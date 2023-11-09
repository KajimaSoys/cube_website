# Generated by Django 4.1.7 on 2023-10-25 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_alter_news_created_alter_reviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 25, 0, 17, 10, 585590, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 25, 0, 17, 10, 585755, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]