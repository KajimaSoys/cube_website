from rest_framework import serializers
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
        fields = ['id', 'category', 'category_info', 'name', 'in_stock', 'size', 'material', 'order', 'images', 'prices']

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
        fields = ['id', 'category_info', 'name', 'description', 'in_stock', 'size', 'material', 'images', 'prices']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Сортировка prices по полю count
        representation['prices'] = sorted(representation['prices'], key=lambda x: x['count'])
        return representation


class ProductInfoSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = ProductInfo
        fields = ('product_id', 'count', 'price')


class OrderSerializer(serializers.ModelSerializer):
    products = ProductInfoSerializer(many=True, source='productinfo_set')

    class Meta:
        model = Orders
        fields = ('uuid', 'phone_number', 'name', 'pickup', 'address', 'products', 'total')
        extra_kwargs = {'uuid': {'read_only': True}}

    def create(self, validated_data):
        products_data = validated_data.pop('productinfo_set')
        order = Orders.objects.create(**validated_data)
        for product_data in products_data:
            ProductInfo.objects.create(order=order, **product_data)
        return order
