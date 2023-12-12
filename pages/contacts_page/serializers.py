from rest_framework import serializers
from pages.contacts_page.models import (
    OutsideView
)


class OutsideViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsideView
        fields = "__all__"
