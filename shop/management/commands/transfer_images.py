from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from shop.models import Product, ProductImage


class Command(BaseCommand):
    help = 'Переносит изображения из Product.image в ProductImage.image'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            if product.image:
                # Создание новой записи в модели ProductImage
                product_image = ProductImage(product=product)

                # Сохранение изображения из Product в ProductImage
                product_image.image.save(
                    product.image.name,
                    ContentFile(product.image.read()),
                    save=True
                )

                self.stdout.write(self.style.SUCCESS(f'Successfully transferred image for product {product.name}'))
