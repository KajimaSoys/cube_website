from django.contrib import admin
from django.utils.html import mark_safe
from service.models import Reviews
from adminsortable2.admin import SortableAdminMixin


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return mark_safe(f'<a href="{image.url}"><img src="{image.url}" width="250" /></a>')
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
