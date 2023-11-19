from django.contrib import admin
from pages.delivery_page.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
