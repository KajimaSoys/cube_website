from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import mark_safe, format_html
from django.urls import path, reverse
from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import urlparse, parse_qs

from .models import Category, Product, Orders, ProductPrice, ProductImage, ProductList


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


class ProductPriceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductPrice
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(ProductPriceInline, self).get_formset(request, obj, **kwargs)
        form = formset.form
        form.base_fields['count'].initial = 100
        return formset


class ProductImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductImage
    extra = 1

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}"><img src="{obj.image.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните товар для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']


class ProductListInline(admin.StackedInline):
    model = ProductList
    extra = 1
    autocomplete_fields = ('product',)


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Настройки для товаров"""
    list_display = ['name', 'price_1', 'price_at_count_100', 'in_stock']
    list_filter = ['in_stock', 'category']
    list_editable = ['in_stock', 'price_1', ]
    search_fields = ['material', 'name']
    list_display_links = ['name']
    autocomplete_fields = ['category', ]
    form = ProductAdminForm
    inlines = [ProductPriceInline, ProductImageInline]
    # price_at_count_1.short_description = "Цена при 1шт."

    fieldsets = [
        ('Основная информация', {
            'fields': [
                'category', 'name', 'description', 'in_stock',
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
    list_display = ['name', 'get_orders']
    list_display_links = ['name']

    inlines = [ProductListInline]

    fieldsets = [
        (None, {
            'fields': [
                'id',
                'phone_number',
                'name',
                'address',
                'created_at',
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
            'js/orders_fields.js'
        )