from django.contrib import admin
from django.utils.html import mark_safe

from pages.common_elements.models import (
    HeaderBlock,
    RecommendedProductBlock,
    AddQuestionBlock,
)

from adminsortable2.admin import SortableAdminMixin


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'logo',
                'thumbnail',
                'number',
                'mail',
                'address',
                'yandex_map_link',
                'tg_link',
                'whatsapp_link',
            ],
        }),
    ]

    def thumbnail(self, obj):
        if obj.logo:
            return mark_safe(f'<a href="{obj.logo.url}"><img src="{obj.logo.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."

    thumbnail.short_description = "Предпросмотр логотипа"
    readonly_fields = ['thumbnail']


@admin.register(RecommendedProductBlock)
class RecommendedProductBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'product')


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}"><img src="{obj.image.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']
