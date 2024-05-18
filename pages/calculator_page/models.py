from django.db import models
from shop.models import Product


class AdditionalProductBlock(models.Model):
    """
    Description of AdditionalProductBlock Model of Calculator Page App.

    Fields:
    - order: Order of the product;
    - product: Product.
    """

    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name="Порядок"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Товар",
        related_name="additional_product"
    )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'дополнительный товар'
        verbose_name_plural = '1 - Дополнительные товары'
        ordering = ['order', ]
