# Generated by Django 4.1.7 on 2023-12-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_elements', '0004_alter_addquestionblock_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerblock',
            name='yandex_map_link',
            field=models.CharField(default='', max_length=500, verbose_name='Ссылка на Яндекс Карты'),
        ),
    ]
