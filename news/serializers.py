from rest_framework import serializers
from news.models import (
    News,
    Reviews,
)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
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
        model = Reviews
        fields = "__all__"
