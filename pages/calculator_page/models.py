from django.db import models
from ckeditor.fields import RichTextField
from shop.models import Product


class CalculatorDescriptionBlock(models.Model):
    """
    Description of CalculatorDescriptionBlock Model of Calculator Page App.

    Fields:
    - title: Title;
    - description: Description;
    - image: Image.
    """

    title = RichTextField(verbose_name='Заголовок')
    description = models.CharField(verbose_name='Описание', max_length=500)

    image = models.FileField(verbose_name='Фото', upload_to='calculator_page/calculator_description/', max_length=500)

    def __str__(self):
        return 'Описание калькулятора'

    class Meta:
        verbose_name = '1 - Описание калькулятора'
        verbose_name_plural = '1 - Описание калькулятора'


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
        verbose_name_plural = '2 - Дополнительные товары'
        ordering = ['order', ]
