from django.contrib import admin
from pages.calculator_page.models import AdditionalProductBlock
from adminsortable2.admin import SortableAdminMixin


@admin.register(AdditionalProductBlock)
class NewProductBlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'product')
    autocomplete_fields = ('product', )
