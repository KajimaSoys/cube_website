from django.contrib import admin
from pages.product_page.models import Dummy


@admin.register(Dummy)
class DummyAdmin(admin.ModelAdmin):
    pass
