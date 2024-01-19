from django.http import JsonResponse, HttpResponse
from django.conf import settings

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
import requests
from django.conf import settings


######################################################
#                      New views                     #
######################################################


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

        send_sms(order)

        return JsonResponse({'order_number': order.id}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_sms(order):
    message = (f'Поступил заказ №{order.id}\n'
               f'Дата: {order.created_at.strftime("%d.%m.%Y %H:%M:%S")}')

    send_data = {
        'api_id': settings.SMSRU_APIKEY,
        'to': settings.SMSRU_CLIENT,
        'msg': message,
        'json': 1
    }
    print(send_data)
    result = requests.post(url='https://sms.ru/sms/send', data=send_data)
    if result.status_code == 200:
        json_data = result.json()
        print(json_data)
    else:
        print("Ошибка запроса:", result.status_code)


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
