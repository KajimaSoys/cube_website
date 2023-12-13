from rest_framework import serializers
from pages.common_elements.models import (
    HeaderBlock,
    RecommendedProductBlock,
    AddQuestionBlock,
)


class HeaderBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderBlock
        fields = "__all__"


class RecommendedProductBlockSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        from shop.serializers import ProductSerializer

        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        return representation

    class Meta:
        model = RecommendedProductBlock
        fields = "__all__"


class AddQuestionBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddQuestionBlock
        fields = "__all__"


