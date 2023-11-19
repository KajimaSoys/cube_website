from django.contrib import admin
from pages.catalog_page.models import AddQuestionBlock
from django.utils.html import mark_safe


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}"><img src="{obj.image.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']
