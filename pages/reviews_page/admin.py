from django.contrib import admin
from pages.reviews_page.models import Dummy


@admin.register(Dummy)
class DummyAdmin(admin.ModelAdmin):
    pass
