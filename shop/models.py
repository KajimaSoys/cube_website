from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django_resized import ResizedImageField
import uuid
import re
from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


def default_id():
    id_list = Orders.objects.values_list('id', flat=True).distinct()
    if not id_list:
        max_id = 0
    else:
        max_id = max(id_list)
    max_id += 1
    return max_id


def default_date():
    return datetime.now()


class Category(models.Model):
    """
    Model Category of Shop App
    """
    name = models.CharField(max_length=70, verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=70, unique=True, verbose_name='Транслитерация')
    image_cat = models.ImageField(verbose_name='Фотография категории', upload_to='shop/images_cat')
    image_cat_thumbnail = ImageSpecField(source='image_cat', processors=[ResizeToFill(200, 300)], format='jpeg')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True, verbose_name="Порядок")

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['order', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/all_product_category/{self.slug}"


class Product(models.Model):
    """
    Model Product of Shop App
    """
    category = models.ForeignKey(Category, verbose_name='Выберите категорию товара', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование', max_length=100)
    description = models.TextField(verbose_name='Описание товара', help_text='Введите подробное описание товара')
    in_stock = models.BooleanField(verbose_name="В наличии", default=True)

    size = models.CharField(verbose_name='Размер', max_length=30, blank=True, null=True)
    material = models.CharField(verbose_name='Материал', max_length=50, blank=True, null=True)

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Порядок")

    # TODO delete image, image_thumbnail, price_1 fields from model
    image = models.ImageField(verbose_name='Фотография товара (deprecated)', upload_to='shop/images')
    image_thumbnail = ImageSpecField(source='image', processors=ResizeToFill(220, 310), format='jpeg')
    price_1 = models.FloatField(verbose_name='Цена от 1 шт', blank=False)

    def price_at_count_100(self):
        price_obj = self.prices.filter(count=100).first()
        return price_obj.price if price_obj else None
    price_at_count_100.short_description = "От 100 шт"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [models.Index(fields=['name', ])]
        ordering = ['order', ]

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def update_product_price(sender, instance, **kwargs):
    print('Product change')
    ProductPrice.objects.update_or_create(
        product=instance,
        count=1,
        defaults={'price': instance.price_1}
    )


class ProductPrice(models.Model):
    """
    Model ProductPrice of Shop App.
    This model holds the pricing information for different quantities of a product.
    """
    product = models.ForeignKey(Product, related_name='prices', on_delete=models.CASCADE, verbose_name='Товар')
    count = models.PositiveIntegerField(verbose_name='Кол-во товара',
                                        help_text='От какого кол-ва товара начинает действовать оптовая цена')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена',
                                help_text='Цена за ед. товара при указанном кол-ве товара')
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Порядок")

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        unique_together = ('product', 'count')
        ordering = ['order', ]

    def __str__(self):
        return f'При заказе от {self.count}шт. стоимость за ед. {self.price}руб.'


@receiver(pre_save, sender=ProductPrice)
def update_product_price_1(sender, instance, **kwargs):
    print('ProductPrice change')
    if instance.count == 1:
        try:
            target_product = Product.objects.get(pk=instance.product.pk)
            if target_product.price_1 != instance.price:
                target_product.price_1 = instance.price
                target_product.save(update_fields=['price_1'])
        except Product.DoesNotExist:
            pass


class ProductImage(models.Model):
    """
    Model ProductImage of Shop App
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = ResizedImageField(upload_to='shop/images',
                              verbose_name='Фотография товара',
                              size=[1260, 945],
                              quality=85, )
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    class Meta:
        verbose_name = "Фотография товара"
        verbose_name_plural = "Фотографии товаров"
        ordering = ['order', ]

    def __str__(self):
        return self.product.name


class Orders(models.Model):
    """
    Model Orders of Shop App
    """
    uuid = models.UUIDField(verbose_name='Номер заказа', primary_key=True, default=uuid.uuid4, editable=False)
    id = models.BigIntegerField(verbose_name='Номер заказа', default=default_id)

    phone_number = models.CharField(verbose_name='Номер телефона', max_length=30)
    name = models.CharField(verbose_name='ФИО', max_length=30)
    pickup = models.BooleanField(verbose_name='Самовывоз', default=True)
    address = models.CharField(verbose_name='Адрес доставки', max_length=70, default='', blank=True)

    whatsapp_link = models.URLField(verbose_name='Ссылка на WhatsApp', max_length=100, blank=True)
    comment = models.TextField(verbose_name='Комментарий к заказу', blank=True)
    order_status_choices = (
        ('created', 'Заказ создан'),
        ('material_purchase', 'Закупка сырья'),
        ('felling', 'Вырубка'),
        ('packing', 'На упаковке'),
        ('ready_on_stock', 'Готов на складе'),
        ('ready_on_shop', 'Готов в магазине'),
        ('completed', 'Сдан'),
        ('unknown', 'Неизвестно'),
        ('return', 'Возврат'),
    )

    order_status = models.CharField(verbose_name="Статус заказа", choices=order_status_choices,
                                       default='created', max_length=20)

    created_at = models.DateTimeField(verbose_name='Дата создания', default=default_date)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    total = models.DecimalField(verbose_name='Итоговая стоимость, руб.', default=0, decimal_places=2, max_digits=10)

    def get_orders(self):
        return ", ".join([f'{o.product.name} - {o.count}шт, {o.price} руб.' for o in ProductInfo.objects.filter(order_id=self.uuid)])

    get_orders.short_description = "Заказ"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-id', )

    def __str__(self):
        return f'{self.id} - {self.name} - {self.total} рублей'

    def save(self, *args, **kwargs):
        """Создание ссылки на whatsapp"""
        clean_phone = re.sub(r'\D', '', self.phone_number)
        self.whatsapp_link = f'https://wa.me/{clean_phone}'
        super(Orders, self).save(*args, **kwargs)


class ProductInfo(models.Model):
    """
    Model ProductInfo of Shop App
    """
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name='Товар')

    count = models.BigIntegerField(verbose_name='Количество', default=1)
    price = models.DecimalField(verbose_name='Стоимость, руб.', default=0, decimal_places=2, max_digits=10)

    def total(self):
        return self.count * self.price

    def __str__(self):
        return f"{self.product.name}, {self.price} руб. * {self.count} = {self.total()} руб."

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Basket(models.Model):
    """
    Model Basket of Shop App (DISABLED)
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, related_name='product_basket',
                                      verbose_name='Товары добавленные в корзину')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user}'
