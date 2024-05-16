from django import forms
from django.contrib import admin
from django.utils.html import mark_safe, format_html
from django.forms import Textarea
from django.forms.models import BaseInlineFormSet
from django.db import models

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from shop.models import (
    Category,
    Product,
    Orders,
    ProductPrice,
    ProductImage,
    ProductInfo
)


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Настройки для категорий"""
    list_display = ['order', 'name', 'slug', 'thumbnail']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', ]

    def thumbnail(self, obj):
        if obj.image_cat:
            return mark_safe(f'<a href="{obj.image_cat.url}"><img src="{obj.image_cat.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните категорию для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']


class ProductPriceInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Устанавливаем начальное значение поля 'count' на 1 или 100 в зависимости от количества форм
        initial_count_value = 100 if self.instance.pk and self.instance.prices.count() > 0 else 1
        for form in self.forms:
            form.fields['count'].initial = initial_count_value


class ProductPriceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductPrice
    extra = 1
    # formset = ProductPriceInlineFormSet

    # def get_formset(self, request, obj=None, **kwargs):
    #     formset = super(ProductPriceInline, self).get_formset(request, obj, **kwargs)
    #     return formset


class ProductImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductImage
    extra = 1

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}"><img src="{obj.image.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните товар для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']


class ProductInfoInline(admin.StackedInline):
    model = ProductInfo
    extra = 1
    autocomplete_fields = ('product',)


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Настройки для товаров"""
    list_display = ['name', 'price_1', 'price_at_count_100', 'status', 'to_order']
    list_filter = ['status', 'category']
    list_editable = ['status', 'to_order', 'price_1', ]
    search_fields = ['material', 'name']
    list_display_links = ['name']
    autocomplete_fields = ['category', ]
    form = ProductAdminForm
    inlines = [ProductPriceInline, ProductImageInline]

    fieldsets = [
        ('Основная информация', {
            'fields': [
                'category', 'name', 'description', 'status', 'to_order'
            ],
        }),
        ('Характеристики товара', {
            'fields': [
                'size', 'material',
            ],
        }),
    ]


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'get_orders', 'total', 'order_status', 'whatsapp_link_tag', 'comment', ]
    list_display_links = ['name']
    readonly_fields = ['whatsapp_link']
    list_editable = ['comment', 'order_status', ]
    list_filter = ['order_status']

    # def get_search_results(self, request, queryset, search_term):
    #     # Стандартный поиск по полям
    #     queryset, use_distinct = super().get_search_results(request, queryset, search_term)
    #
    #     if search_term:
    #         status_choices = dict(Orders.order_status_choices)
    #         status_values = [key for key, value in status_choices.items() if search_term.lower() in value.lower()]
    #
    #         if status_values:
    #             status_queryset = self.model.objects.filter(order_status__in=status_values)
    #             queryset = queryset.union(status_queryset)
    #
    #     return queryset, use_distinct

    search_fields = (
        'name',
        'id',
        'productinfo__product__name',
        'phone_number',
        'comment'
    )

    search_help_text = 'Доступные для поиска поля: ФИО, номер заказа, заказ, номер телефона, комментарий к заказу'

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }

    inlines = [ProductInfoInline]

    fieldsets = [
        (None, {
            'fields': [
                'id',
                'phone_number',
                'name',
                'pickup',
                'address',
                'created_at',
                'order_status',
                'whatsapp_link',
                'comment',
            ],
        }),
        ('Итого', {
            'fields': [
                'total',
            ],
        }),
    ]

    class Media:
        js = (
            'admin/js/vendor/jquery/jquery.js',
            'js/jquery.maskedinput.js',
            'js/orders/orders_fields.js',
        )

    def whatsapp_link_tag(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.whatsapp_link, obj.whatsapp_link)

    whatsapp_link_tag.short_description = 'Ссылка на WhatsApp'
