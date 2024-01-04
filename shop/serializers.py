from rest_framework import serializers
from shop.models import (
    Category,
    Product,
    ProductPrice,
    ProductImage,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'order']


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ['count', 'price']


class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True) # source='productimage_set'
    prices = ProductPriceSerializer(many=True, read_only=True) # source='prices'
    category_slug = CategorySlugSerializer(source='category')

    class Meta:
        model = Product
        fields = ['id', 'category', 'category_slug', 'name', 'in_stock', 'size', 'material', 'order', 'images', 'prices']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    prices = ProductPriceSerializer(many=True, read_only=True)
    category_info = CategorySerializer(source='category')

    class Meta:
        model = Product
        fields = ['id', 'category_info', 'name', 'description', 'in_stock', 'size', 'material', 'images', 'prices']
