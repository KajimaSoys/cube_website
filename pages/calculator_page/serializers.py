from rest_framework import serializers
from pages.calculator_page.models import (
    CalculatorDescriptionBlock,
    AdditionalProductBlock
)


class CalculatorDescriptionBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorDescriptionBlock
        fields = "__all__"


class AdditionalProductBlockSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        from shop.serializers import ProductSerializer

        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        return representation

    class Meta:
        model = AdditionalProductBlock
        fields = "__all__"
