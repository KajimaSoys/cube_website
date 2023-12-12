# Generated by Django 4.1.7 on 2023-11-23 21:59

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_page', '0004_alter_paymentblock_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentblock',
            name='image_first',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=80, scale=None, size=[300, None], upload_to='delivery_page/payment/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='paymentblock',
            name='image_second',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=80, scale=None, size=[300, None], upload_to='delivery_page/payment/', verbose_name='Фото'),
        ),
    ]