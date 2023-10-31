from django.core.management.base import BaseCommand
from shop.models import Product, ProductPrice


class Command(BaseCommand):
    help = 'Переносит значения из Product.price_1 в ProductPrice.price'

    def handle(self, *args, **kwargs):
        for product in Product.objects.all():
            ProductPrice.objects.update_or_create(
                product=product,
                count=1,
                defaults={'price': product.price_1}
            )
        self.stdout.write(self.style.SUCCESS('Successfully migrated price_1 to ProductPrice'))