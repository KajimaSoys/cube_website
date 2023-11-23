from django.contrib import admin
from pages.about_page.models import Dummy


@admin.register(Dummy)
class DummyAdmin(admin.ModelAdmin):
    pass
