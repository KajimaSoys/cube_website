from django.contrib import admin
from django.utils.html import format_html

from service.models import Reviews
from adminsortable2.admin import SortableAdminMixin


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return format_html('<a href="{0}"><img src="{0}" width="250" /></a>', image.url)
    return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."


@admin.register(Reviews)
class ReviewsAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'review',
                'image',
                'thumbnail',
                'published',
                'creation_date'
            ],
        }),
    ]

    list_display = ['order', 'name', 'review', 'thumbnail', 'published', 'creation_date']
    list_editable = ['published']

    def thumbnail(self, obj):
        return generate_thumbnail(obj, 'image')

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail', 'creation_date']
