from django.contrib import admin
from pages.catalog_page.models import AddQuestionBlock


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    pass
