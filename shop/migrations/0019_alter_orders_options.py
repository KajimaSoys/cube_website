# Generated by Django 4.1.7 on 2024-01-09 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_rename_productlist_productinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('-id',), 'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
    ]