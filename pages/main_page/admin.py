from django.contrib import admin
from django.utils.html import mark_safe

from pages.main_page.models import (
    MainBlock,
    CatalogTeaserBlock,
    ServiceOptionsBlock,
    NewProductBlock,
    PopularProductBlock,
    DeliveryBlock,
    AdvantagesBlock,
    CartonInfoBlock,
    RequestBlock,
    QuestionsBlock,
    ContactsBlock,
)

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


def generate_thumbnail(obj, image_field):
    image = getattr(obj, image_field, None)
    if image:
        return mark_safe(f'<a href="{image.url}"><img src="{image.url}" width="200" /></a>')
    return "Предпросмотр пока недоступен. Добавьте фото и сохраните объект для отображения фото."


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        return generate_thumbnail(obj, 'image')

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']


@admin.register(CatalogTeaserBlock)
class CatalogTeaserBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceOptionsBlock)
class ServiceOptionsBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
            ],
        }),
        ('Карточка №1', {
            'fields': [
                'option_first',
                'image_first',
                'thumbnail_first',
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'option_second',
                'image_second',
                'thumbnail_second',
            ],
        }),
        ('Карточка №3', {
            'fields': [
                'option_third',
                'image_third',
                'thumbnail_third',
            ],
        }),
    ]

    def thumbnail_first(self, obj):
        return generate_thumbnail(obj, 'image_first')

    def thumbnail_second(self, obj):
        return generate_thumbnail(obj, 'image_second')

    def thumbnail_third(self, obj):
        return generate_thumbnail(obj, 'image_third')

    thumbnails = [thumbnail_first, thumbnail_second, thumbnail_third]
    for thumbnail in thumbnails:
        thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail_first', 'thumbnail_second', 'thumbnail_third']


@admin.register(NewProductBlock)
class NewProductBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'product')


@admin.register(PopularProductBlock)
class PopularProductBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'product')


@admin.register(DeliveryBlock)
class DeliveryBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
            ],
        }),
        ('Карточка №1', {
            'fields': [
                'subtitle_first',
                'text_first',
                'additional_first',
                'image_first',
                'thumbnail_first',
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'subtitle_second',
                'text_second',
                'additional_second',
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


@admin.register(AdvantagesBlock)
class AdvantagesBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
            ],
        }),
        ('Карточка №1', {
            'fields': [
                'subtitle_first',
                'text_first',
                'additional_first',
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'subtitle_second',
                'text_second',
                'additional_second',
            ],
        }),
        ('Карточка №3', {
            'fields': [
                'subtitle_third',
                'text_third',
                'additional_third',
            ],
        }),
        ('Карточка №4', {
            'fields': [
                'subtitle_fourth',
                'text_fourth',
                'additional_fourth',
            ],
        }),
        ('Карточка №5', {
            'fields': [
                'subtitle_fifth',
                'text_fifth',
                'additional_fifth',
            ],
        }),
        ('Карточка №6', {
            'fields': [
                'subtitle_sixth',
                'text_sixth',
                'additional_sixth',
            ],
        }),
    ]


@admin.register(CartonInfoBlock)
class CartonInfoBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'description',
                'quality_block',
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


@admin.register(RequestBlock)
class RequestBlockAdmin(admin.ModelAdmin):

    def thumbnail(self, obj):
        return generate_thumbnail(obj, 'image')

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail', ]


@admin.register(QuestionsBlock)
class QuestionsBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'question', 'answer')


@admin.register(ContactsBlock)
class ContactsBlockAdmin(admin.ModelAdmin):
    pass
