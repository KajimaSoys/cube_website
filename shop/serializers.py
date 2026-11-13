from django.db import transaction
from rest_framework import serializers

from shop.pricing import line_total
from shop.models import (
    Category,
    Product,
    ProductPrice,
    ProductImage,
    ProductInfo,
    Orders
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
    category_info = CategorySlugSerializer(source='category')

    class Meta:
        model = Product
        fields = ['id', 'category', 'category_info', 'name', 'status', 'to_order', 'size', 'material', 'order', 'images', 'prices']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Сортировка prices по полю count
        representation['prices'] = sorted(representation['prices'], key=lambda x: x['count'])
        return representation


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    prices = ProductPriceSerializer(many=True, read_only=True)
    category_info = CategorySerializer(source='category')

    class Meta:
        model = Product
        fields = ['id', 'category_info', 'name', 'description', 'status', 'to_order', 'size', 'material', 'images', 'prices']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Сортировка prices по полю count
        representation['prices'] = sorted(representation['prices'], key=lambda x: x['count'])
        return representation


class ProductInfoSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True)
    count = serializers.IntegerField(min_value=1, max_value=10_000_000)

    class Meta:
        model = ProductInfo
        fields = ('product_id', 'count', 'price')
        # Цену присылает фронт, но доверять ей нельзя: она пересчитывается на сервере по тарифам из БД.
        read_only_fields = ('price',)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductInfoSerializer(many=True, source='productinfo_set', allow_empty=False, max_length=200)

    class Meta:
        model = Orders
        fields = ('uuid', 'phone_number', 'name', 'pickup', 'address', 'products', 'total')
        # total тоже считается на сервере: сумма позиций по ценам из БД.
        read_only_fields = ('uuid', 'total')

    @transaction.atomic
    def create(self, validated_data):
        products_data = validated_data.pop('productinfo_set')
        lines = []
        for item in products_data:
            product = item['product']
            tiers = product.prices.values_list('count', 'price')
            price = line_total(tiers, item['count'])
            if price is None:
                raise serializers.ValidationError({'products': [f'У товара {product.pk} не задана цена']})
            lines.append((product, item['count'], price))

        order = Orders.objects.create(total=sum(p for _, _, p in lines), **validated_data)
        for product, count, price in lines:
            ProductInfo.objects.create(order=order, product=product, count=count, price=price)
        return order
