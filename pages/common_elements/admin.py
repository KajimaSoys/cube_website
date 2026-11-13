from django.contrib import admin
from django.utils.html import format_html

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
                'vk_link',
                'whatsapp_link',
                'max_link',
            ],
        }),
    ]

    def thumbnail(self, obj):
        if obj.logo:
            return format_html('<a href="{0}"><img src="{0}" width="200" /></a>', obj.logo.url)
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
            return format_html('<a href="{0}"><img src="{0}" width="200" /></a>', obj.image.url)
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']
