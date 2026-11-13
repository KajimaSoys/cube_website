from django.contrib import admin
from django.utils.html import format_html

from pages.catalog_page.models import AddQuestionBlock


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<a href="{0}"><img src="{0}" width="200" /></a>', obj.image.url)
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']
