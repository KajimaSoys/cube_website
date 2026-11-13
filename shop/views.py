from django.http import JsonResponse, HttpResponse

from shop.models import (
    Category,
    Product,
    ProductPrice
)
from shop.serializers import (
    ProductListSerializer,
    CategorySerializer,
    ProductSerializer,
    OrderSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import hmac
import hashlib
import json

from django.conf import settings

from shop.notifications import send_order_email
from shop.pricing import unit_price


# Сколько товаров можно запросить одним POST /api/v1/products/ (корзина).
MAX_CART_ITEMS = 200


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Product.objects.select_related('category').prefetch_related('images', 'prices')
        elif self.request.method == 'POST':
            # Корзина из localStorage: [{"id": 1, "quantity": 2}, ...]. Мусорный ввод — пустой ответ, а не 500.
            data = self.request.data if isinstance(self.request.data, list) else []
            ids = []
            for item in data[:MAX_CART_ITEMS]:
                if isinstance(item, dict):
                    try:
                        ids.append(int(item.get('id')))
                    except (TypeError, ValueError):
                        continue
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

    if not isinstance(request.data, dict) or not isinstance(request.data.get('request'), dict):
        return JsonResponse({'request': ['Обязательное поле.']}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderSerializer(data=request.data['request'])
    if serializer.is_valid():
        order = serializer.save()

        send_order_email(order)

        return JsonResponse({'order_number': order.id}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProductPrice(APIView):
    queryset = ProductPrice.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            product_id = int(request.GET['product_id'])
        except KeyError:
            return Response({'error': 'product_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'product_id must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            count = int(request.GET.get('count', 1))
        except ValueError:
            return Response({'error': 'count must be an integer'}, status=status.HTTP_400_BAD_REQUEST)
        if count < 1:
            return Response({'error': 'count must be >= 1'}, status=status.HTTP_400_BAD_REQUEST)

        tiers = ProductPrice.objects.filter(product_id=product_id).values_list('count', 'price')
        price = unit_price(tiers, count)
        if price is None:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'price': price}, status=status.HTTP_200_OK)
