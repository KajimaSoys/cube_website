from rest_framework import serializers
from pages.main_page.models import (
    MainBlock,
    CatalogTeaserBlock,
    ServiceOptionsBlock,
    NewProductBlock,
    PopularProductBlock,
    DeliveryBlock,
    AdvantagesBlock,
    CartonInfoBlock,
    RequestBlock,
    QuestionsBlock,
    ContactsBlock,
)


class MainBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBlock
        fields = "__all__"


class CatalogTeaserBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogTeaserBlock
        fields = "__all__"


class ServiceOptionsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOptionsBlock
        fields = "__all__"


class NewProductBlockSerializer(serializers.ModelSerializer):
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
        model = NewProductBlock
        fields = "__all__"


class PopularProductBlockSerializer(serializers.ModelSerializer):
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
        model = PopularProductBlock
        fields = "__all__"


class DeliveryBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBlock
        fields = "__all__"


class AdvantagesBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesBlock
        fields = "__all__"


class CartonInfoBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartonInfoBlock
        fields = "__all__"


class RequestBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestBlock
        fields = "__all__"


class QuestionsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsBlock
        fields = "__all__"


class ContactsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsBlock
        fields = "__all__"