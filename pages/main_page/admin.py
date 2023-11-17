from django.contrib import admin
from pages.main_page.models import (
    HeaderBlock,
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
    AddQuestionBlock,
)
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    pass


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
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'option_second',
                'image_second',
            ],
        }),
        ('Карточка №3', {
            'fields': [
                'option_third',
                'image_third',
            ],
        }),
    ]


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
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'subtitle_second',
                'text_second',
                'additional_second',
                'image_second',
            ],
        }),
    ]


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
            ],
        }),
        ('Карточка №2', {
            'fields': [
                'subtitle_second',
                'text_second',
                'image_second',
            ],
        }),
    ]


@admin.register(RequestBlock)
class RequestBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionsBlock)
class QuestionsBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'question', 'answer')


@admin.register(ContactsBlock)
class ContactsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    pass


