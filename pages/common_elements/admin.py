from django.contrib import admin
from pages.common_elements.models import (
    HeaderBlock,
    RecommendedProductBlock,
    AddQuestionBlock,
)
from adminsortable2.admin import SortableAdminMixin


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(RecommendedProductBlock)
class RecommendedProductBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'product')


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    pass
