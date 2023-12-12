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
    # TODO add representation method
    # def to_representation(self, instance):
    #
    #     from core.catalog.serializers import SofaListSerializer
    #
    #     representation = super().to_representation(instance)
    #     representation['sofa'] = SofaListSerializer(instance.sofa).data
    #     return representation
    #
    # class Meta:
    #     model = NewProductBlock
    #     fields = ['order', 'product']
    class Meta:
        model = RecommendedProductBlock
        fields = "__all__"


class AddQuestionBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddQuestionBlock
        fields = "__all__"


