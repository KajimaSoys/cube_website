# Generated by Django 4.1.7 on 2023-10-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_brand_of_cardboard_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['order'], 'verbose_name': 'Фотография товара', 'verbose_name_plural': 'Фотографии товаров'},
        ),
        migrations.AddField(
            model_name='productimage',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок'),
        ),
    ]
