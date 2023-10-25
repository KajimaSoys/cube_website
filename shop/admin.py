from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import mark_safe

from .models import Category, Product, Orders, ProductImage, ProductList


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Настройки для категорий"""
    list_display = ['slug', 'name',  'order']
    list_editable = ['name']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


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
    extra = 0
    autocomplete_fields = ('product',)


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Настройки для товаров"""
    list_display = ['name', 'price_1', 'in_stock']
    list_filter = ['in_stock', 'category']
    list_editable = ['in_stock', 'price_1', ]
    search_fields = ['material', 'name']
    list_display_links = ['name']
    form = ProductAdminForm
    inlines = [ProductImageInline]


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_orders']
    list_display_links = ['name']

    inlines = [ProductListInline]
