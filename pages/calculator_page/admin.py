from django.contrib import admin
from django.utils.html import mark_safe

from pages.calculator_page.models import (
    CalculatorDescriptionBlock,
    AdditionalProductBlock
)
from adminsortable2.admin import SortableAdminMixin


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return mark_safe(f'<a href="{image.url}"><img src="{image.url}" width="200" /></a>')
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
