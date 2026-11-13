from django.contrib import admin
from django.utils.html import format_html

from pages.delivery_page.models import PaymentBlock


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return format_html('<a href="{0}"><img src="{0}" width="200" /></a>', image.url)
    return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."


@admin.register(PaymentBlock)
class PaymentBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'question_link',
            ],
        }),
        ('Карточка №1', {
            'fields': [
                'subtitle_first',
                'text_first',
                'image_first',
                'thumbnail_first',
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'subtitle_second',
                'text_second',
                'image_second',
                'thumbnail_second',
            ],
        }),

    ]

    def thumbnail_first(self, obj):
        return generate_thumbnail(obj, 'image_first')

    def thumbnail_second(self, obj):
        return generate_thumbnail(obj, 'image_second')

    thumbnails = [thumbnail_first, thumbnail_second]
    for thumbnail in thumbnails:
        thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail_first', 'thumbnail_second']
