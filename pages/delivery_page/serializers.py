from rest_framework import serializers
from pages.delivery_page.models import (
    PaymentBlock
)


class PaymentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentBlock
        fields = "__all__"
