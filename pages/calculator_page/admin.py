from django.contrib import admin
from django.utils.html import format_html

from pages.calculator_page.models import (
    CalculatorDescriptionBlock,
    AdditionalProductBlock
)
from adminsortable2.admin import SortableAdminMixin


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return format_html('<a href="{0}"><img src="{0}" width="200" /></a>', image.url)
    return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."


@admin.register(CalculatorDescriptionBlock)
class CalculatorDescriptionBlockAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return generate_thumbnail(obj, 'image')

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail', ]


@admin.register(AdditionalProductBlock)
class NewProductBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'product')
    autocomplete_fields = ('product', )
