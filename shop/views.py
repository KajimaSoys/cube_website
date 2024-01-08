from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.conf import settings

from shop.models import (
    Category,
    Product,
    Basket,
    ProductInfo,
    Orders,
    ProductImage,
    ProductPrice
)

from shop.serializers import (
    ProductListSerializer,
    CategorySerializer,
    ProductSerializer,
    OrderSerializer
)


from shop.forms import OrderForm
from shop.services import send_sms

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import hmac
import hashlib
import json


######################################################
#                      New views                     #
######################################################


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.select_related('category').prefetch_related('images', 'prices')
#     serializer_class = ProductListSerializer

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Product.objects.select_related('category').prefetch_related('images', 'prices')
        elif self.request.method == 'POST':
            ids = [item['id'] for item in self.request.data if 'id' in item]
            if not ids:
                return Product.objects.none()  # Возвращает пустой QuerySet
            return Product.objects.filter(id__in=ids).select_related('category').prefetch_related('images', 'prices')

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug).prefetch_related('images', 'prices')


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Product.objects.filter(id=product_id).select_related('category').prefetch_related('images', 'prices')


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_order(request):
    hmac_key = settings.HMAC_KEY
    received_signature = request.META.get("HTTP_X_SIGNATURE")

    if received_signature:
        payload = json.dumps(request.data, separators=(",", ":"), ensure_ascii=False)
        expected_signature = hmac.new(bytes(hmac_key, 'utf-8'), msg=payload.encode("utf-8"),
                                      digestmod=hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected_signature, received_signature):
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)

    serializer = OrderSerializer(data=request.data['request'])
    if serializer.is_valid():
        order = serializer.save()
        # TODO Добавить отправку смс после создания заказа
        return JsonResponse({'order_number': order.id}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO понять необходимость этого представления -> Удалить представление
class GetProductPrice(APIView):
    queryset = ProductPrice.objects.all()

    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id')
        count = int(request.GET.get('count', 0))

        if not product_id:
            return Response({'error': 'product_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Получаем все цены для данного продукта, отсортированные по количеству
            product_prices = ProductPrice.objects.filter(product_id=product_id).order_by('count')

            # Ищем подходящую цену на основе заданного количества
            for product_price in product_prices:
                if count >= product_price.count:
                    price = product_price.price
        except ProductPrice.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'price': price}, status=status.HTTP_200_OK)


######################################################
#                      Old views                     #
######################################################


class HomeView(TemplateView):
    """Home page"""
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Картонные коробки в Казани. Интернет-магазин cubekazan.ru'
        return context


class CategoryList(ListView):
    """View which present all category"""
    model = Category
    context_object_name = 'cat'
    template_name = 'shop/all_category.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        return context


class AllProductCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/all_product_category.html'

    def get_queryset(self):
        return self.model.objects.filter(category__slug=self.kwargs['slug'], in_stock=True).select_related(
            'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробности о товаре'
        context['categories'] = Category.objects.all()
        context['images'] = ProductImage.objects.filter(product__pk=self.kwargs['product_pk'])
        return context


class ImagesListView(ListView):
    template_name = 'shop/test.html'
    model = ProductImage
    context_object_name = 'images'

@login_required(login_url='login_user')
def add_to_basket(request, product_pk):
    book = get_object_or_404(Product, pk=product_pk)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket.products.add(book)
    basket.save()
    messages.info(request, 'Товар добавлен в корзину')
    return redirect('product_detail', product_pk=product_pk)


@login_required(login_url='login_user')
def add_product(request, product_pk):
    book = get_object_or_404(Product, pk=product_pk)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket.products.add(book)
    basket.save()
    messages.info(request, 'Товар добавлен в корзину')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def show_basket(request):
    try:
        form = OrderForm()
        user_basket = Basket.objects.prefetch_related('products').get(user=request.user.id)
        products = user_basket.products.all()

        return render(request, 'shop/show_basket.html',
                      {'user_basket': user_basket, 'products': products, 'form': form, 'title': 'Корзина'})
    except Exception:
        return render(request, 'shop/show_basket.html', {'message': 'Корзина пуста', 'title': 'Корзина'})
    except AttributeError as ext:

        return render(request, 'shop/show_basket.html', {'message': 'Корзина пуста', 'title': 'Корзина'})


@login_required
def delete_product(request, product_pk):
    user_basket = Basket.objects.get(user=request.user.id)

    product = get_object_or_404(Product, pk=product_pk)
    user_basket.products.remove(product)
    user_basket.save()

    return redirect('show_basket')

#
# @login_required
# def create_order(request):
#     if request.method == 'POST':
#         user = request.user
#         name = request.POST['name']
#         address = request.POST['address']
#         created = timezone.now()
#         phone_number = request.POST['phone_number']
#         check_fields = (name, phone_number)
#         if all(check_fields):
#             order = Orders.objects.create(user=user, name=name,
#                                           phone_number=phone_number, created=created, address=address)
#             try:
#                 basket = Basket.objects.get(user=request.user)
#                 products = basket.products.all()
#                 for product in products:
#                     order.products.add(product)
#                 order.save()
#                 send_sms(request)
#                 basket.delete()
#                 messages.info(request, 'Товар оформлен, с вами свяжутся')
#                 return redirect('show_basket')
#             except ValueError:
#                 message = 'Введите данные или добавьте товар в корзину'
#                 return render(request, 'shop/show_basket.html', context={'message': message})
#
#         else:
#             return render(request, 'shop/show_basket.html',
#                           context={'message': 'Введите данные или добавьте товар в корзину'})


# View для Auth
def sigh_up(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'shop/signup.html', {'form': UserCreationForm(),
                                                            'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'shop/signup.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'shop/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')
