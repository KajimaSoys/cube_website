from rest_framework import serializers
from pages.catalog_page.models import AddQuestionBlock


class AddQuestionBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddQuestionBlock
        fields = "__all__"
