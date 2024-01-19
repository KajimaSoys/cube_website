from django.urls import path
from shop.views import GetProductPrice

urlpatterns = [
    path('api/v1/get_price/', GetProductPrice.as_view(), name='get-product-price'),
]
