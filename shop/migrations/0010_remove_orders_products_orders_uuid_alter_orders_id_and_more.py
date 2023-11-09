# Generated by Django 4.1.7 on 2023-10-25 00:26

from django.db import migrations, models
import shop.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='products',
        ),
        migrations.AddField(
            model_name='orders',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.BigIntegerField(default=shop.models.default_id, verbose_name='Номер заказа'),
        ),
        migrations.DeleteModel(
            name='ProductList',
        ),
    ]