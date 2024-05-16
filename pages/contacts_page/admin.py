from django.contrib import admin
from django.utils.html import mark_safe

from pages.contacts_page.models import OutsideView


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return mark_safe(f'<a href="{image.url}"><img src="{image.url}" width="200" /></a>')
    return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."


@admin.register(OutsideView)
class OutsideViewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Карточка №1', {
            'fields': [
                'image_first',
                'thumbnail_first',
                'text_first',
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'image_second',
                'thumbnail_second',
                'text_second',
            ],
        }),
        ('Карточка №3', {
            'fields': [
                'image_third',
                'thumbnail_third',
                'text_third',
            ],
        }),
    ]

    def thumbnail_first(self, obj):
        return generate_thumbnail(obj, 'image_first')

    def thumbnail_second(self, obj):
        return generate_thumbnail(obj, 'image_second')

    def thumbnail_third(self, obj):
        return generate_thumbnail(obj, 'image_third')

    thumbnails = [thumbnail_first, thumbnail_second]
    for thumbnail in thumbnails:
        thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail_first', 'thumbnail_second', 'thumbnail_third']
