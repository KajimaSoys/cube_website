from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from django_resized import ResizedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import uuid
import re
from datetime import datetime


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
    Model Category of Shop App.

    Fields:
    - id: Primary key, auto-incremented;
    - name: The name of the category;
    - slug: Unique slug for the category;
    - image_cat: Category image;
    - image_cat_thumbnail: Thumbnail of the category image;
    - order: Order of the category.
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
    Model Product of Shop App.

    Fields:
    - id: Primary key, auto-incremented;
    - category: Foreign key to Category;
    - name: Name of the product;
    - description: Description of the product;
    - status: Status of the product (choices: in_stock, out_of_stock, to_order);
    - to_order: Quantity of products to order;
    - size: Size of the product;
    - material: Material of the product;
    - order: Order of the product;
    - price_1: Price per unit.
    """

    category = models.ForeignKey(Category, verbose_name='Выберите категорию товара', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование', max_length=100)
    description = models.TextField(verbose_name='Описание товара', help_text='Введите подробное описание товара')

    STATUS_CHOICES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Отсутствует'),
        ('to_order', 'Под заказ')
    )
    status = models.CharField(verbose_name='Статус товара', choices=STATUS_CHOICES, max_length=20, default='in_stock')
    to_order = models.IntegerField(
        verbose_name='Кол-во товаров под заказ',
        blank=True,
        null=True,
        help_text='Если статус товара "Под заказ" нужно ввести кол-во товаров'
    )

    size = models.CharField(verbose_name='Размер', max_length=30, blank=True, null=True)
    material = models.CharField(verbose_name='Материал', max_length=50, blank=True, null=True)

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Порядок")

    price_1 = models.FloatField(verbose_name='Цена от 1 шт', blank=False, null=True)

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


@receiver(post_delete, sender=Product)
def delete_post_session_files(sender, instance, **kwargs):
    """
    Signal handler to delete associated files on PostSession deletion.
    """
    images = ProductImage.objects.filter(product=instance)
    for image in images:
        if image.image:
            image.image.delete(save=False)


class ProductPrice(models.Model):
    """
    Model ProductPrice of Shop App.

    This model holds the pricing information for different quantities of a product.

    Fields:
    - id: Primary key, auto-incremented;
    - product: Foreign key to Product;
    - count: Quantity of product;
    - price: Price per unit for the given quantity;
    - order: Order of the pricing record.
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


# Глобальная переменная для отслеживания состояния обновления
is_updating_from_product_price = False


@receiver(post_save, sender=Product)
def update_product_price(sender, instance, **kwargs):
    global is_updating_from_product_price

    if is_updating_from_product_price:
        return

    if instance.price_1 is not None:
        existing_price = ProductPrice.objects.filter(product=instance, count=1).first()
        if existing_price:
            existing_price.price = instance.price_1
            existing_price.save()
        else:
            ProductPrice.objects.create(product=instance, count=1, price=instance.price_1)


@receiver(pre_save, sender=ProductPrice)
def update_product_price_1(sender, instance, **kwargs):
    global is_updating_from_product_price

    if instance.count == 1:
        target_product = Product.objects.get(pk=instance.product.pk)
        if target_product.price_1 != instance.price:
            is_updating_from_product_price = True
            target_product.price_1 = instance.price
            target_product.save(update_fields=['price_1'])
            is_updating_from_product_price = False


class ProductImage(models.Model):
    """
    Model ProductImage of Shop App.

    Fields:
    - id: Primary key, auto-incremented;
    - product: Foreign key to Product;
    - image: Image of the product;
    - order: Order of the image.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = ResizedImageField(upload_to='shop/images',
                              verbose_name='Фотография товара',
                              size=[570, 470],
                              quality=75, )
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    class Meta:
        verbose_name = "Фотография товара"
        verbose_name_plural = "Фотографии товаров"
        ordering = ['order', ]

    def __str__(self):
        return self.product.name


@receiver(post_delete, sender=ProductImage)
def delete_image_file(sender, instance, **kwargs):
    """
    Signal handler to delete image file on ProductImage deletion.
    """
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=ProductImage)
def delete_old_image_file(sender, instance, **kwargs):
    """
    Signal handler to delete old image file on ProductImage update.
    """
    if instance.pk:
        # Получаем предыдущий объект из базы данных
        old_instance = sender.objects.get(pk=instance.pk)
        # Проверяем, изменилось ли изображение
        if old_instance.image and old_instance.image != instance.image:
            old_instance.image.delete(save=False)


class Orders(models.Model):
    """
    Model Orders of Shop App.

    Fields:
    - uuid: Unique identifier for the order;
    - id: Order number;
    - phone_number: Customer's phone number;
    - name: Customer's name;
    - pickup: Whether the order is for pickup;
    - address: Delivery address;
    - whatsapp_link: Link to WhatsApp for customer communication;
    - comment: Customer's comment for the order;
    - order_status: Status of the order;
    - created_at: Date and time when the order was created;
    - updated_at: Date and time when the order was last updated;
    - total: Total cost of the order.
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
    Model ProductInfo of Shop App.

    Fields:
    - id: Primary key, auto-incremented;
    - order: Foreign key to Orders;
    - product: Foreign key to Product;
    - count: Quantity of the product;
    - price: Price per unit.
    """

    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name='Товар')

    count = models.BigIntegerField(verbose_name='Количество', default=1)
    price = models.DecimalField(verbose_name='Стоимость, руб.', default=0, decimal_places=2, max_digits=10)

    def total(self):
        return self.count * self.price

    def __str__(self):
        return f"{self.product.name} - {self.count}шт, {self.price} руб."

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
