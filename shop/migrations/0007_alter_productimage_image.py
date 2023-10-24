# Generated by Django 4.1.7 on 2023-10-22 17:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_productimage_options_productimage_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=85, scale=None, size=[1260, 945], upload_to='shop/images', verbose_name='Фотография товара'),
        ),
    ]
