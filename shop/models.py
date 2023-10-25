from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django_resized import ResizedImageField
import uuid
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
    Model Category of Shop App
    """
    name = models.CharField(max_length=70, verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=70, unique=True)
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
    name = models.CharField(verbose_name='Имя товара', max_length=100)
    description = models.TextField(verbose_name='Описание товара', help_text='Введите подробное описание товара')
    size = models.CharField(verbose_name='Размеры Товара', max_length=30, blank=True, null=True)
    material = models.CharField(verbose_name='Материал', max_length=50, blank=True, null=True)
    price_1 = models.FloatField(verbose_name='Цена от 1', blank=False)

    # TODO delete field from model
    image = models.ImageField(verbose_name='Фотография товара', upload_to='shop/images')

    in_stock = models.BooleanField(verbose_name="В наличии", default=True)
    category = models.ForeignKey(Category, verbose_name='Выберите категорию товара', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
        verbose_name="Порядок")
    image_thumbnail = ImageSpecField(source='image', processors=ResizeToFill(220, 310), format='jpeg')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [models.Index(fields=['name', ])]
        ordering = ['order', ]

    def __str__(self):
        return self.name


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

    phone_number = models.CharField(blank=True, verbose_name='Номер телефона', max_length=30)
    name = models.CharField(max_length=30, verbose_name='ФИО', blank=True)
    address = models.CharField(verbose_name='Адрес доставки', max_length=70, default='Чистопольская ул. 7, Казань')

    created_at = models.DateTimeField(verbose_name='Дата создания', default=default_date)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    total = models.DecimalField(verbose_name='Итоговая стоимость, руб.', default=0, decimal_places=2, max_digits=10)

    def get_orders(self):
        return ", ".join([o.product.name for o in ProductList.objects.filter(order_id=self.uuid)])

    get_orders.short_description = "Заказ"

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'{self.id} - {self.name} - {self.total} рублей'


class ProductList(models.Model):
    """
    Model ProductList of Shop App
    """
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name='Товар')

    count = models.BigIntegerField(verbose_name='Количество', default=1)
    price = models.DecimalField(verbose_name='Стоимость, руб.', default=0, decimal_places=2, max_digits=10)

    def total(self):
        return self.count * self.product.price_1

    def __str__(self):
        return f"{self.product.name}, {self.product.price_1} руб. * {self.count} = {self.total()} руб."

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
