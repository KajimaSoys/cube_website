# Generated by Django 4.1.7 on 2024-01-17 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import shop.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='Транслитерация')),
                ('image_cat', models.ImageField(upload_to='shop/images_cat', verbose_name='Фотография категории')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Номер заказа')),
                ('id', models.BigIntegerField(default=shop.models.default_id, verbose_name='Номер заказа')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('name', models.CharField(max_length=30, verbose_name='ФИО')),
                ('pickup', models.BooleanField(default=True, verbose_name='Самовывоз')),
                ('address', models.CharField(blank=True, default='', max_length=70, verbose_name='Адрес доставки')),
                ('whatsapp_link', models.URLField(blank=True, max_length=100, verbose_name='Ссылка на WhatsApp')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий к заказу')),
                ('order_status', models.CharField(choices=[('created', 'Заказ создан'), ('material_purchase', 'Закупка сырья'), ('felling', 'Вырубка'), ('packing', 'На упаковке'), ('ready_on_stock', 'Готов на складе'), ('ready_on_shop', 'Готов в магазине'), ('completed', 'Сдан'), ('unknown', 'Неизвестно'), ('return', 'Возврат')], default='created', max_length=20, verbose_name='Статус заказа')),
                ('created_at', models.DateTimeField(default=shop.models.default_date, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Итоговая стоимость, руб.')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(help_text='Введите подробное описание товара', verbose_name='Описание товара')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
                ('size', models.CharField(blank=True, max_length=30, null=True, verbose_name='Размер')),
                ('material', models.CharField(blank=True, max_length=50, null=True, verbose_name='Материал')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('price_1', models.FloatField(verbose_name='Цена от 1 шт')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Выберите категорию товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.BigIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Стоимость, руб.')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.orders', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=85, scale=None, size=[1260, 945], upload_to='shop/images', verbose_name='Фотография товара')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фотография товара',
                'verbose_name_plural': 'Фотографии товаров',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(related_name='product_basket', to='shop.product', verbose_name='Товары добавленные в корзину')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(help_text='От какого кол-ва товара начинает действовать оптовая цена', verbose_name='Кол-во товара')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена за ед. товара при указанном кол-ве товара', max_digits=10, verbose_name='Цена')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'ordering': ['order'],
                'unique_together': {('product', 'count')},
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='shop_produc_name_a2070e_idx'),
        ),
    ]
