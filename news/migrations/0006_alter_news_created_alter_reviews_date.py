# Generated by Django 4.1.7 on 2023-05-22 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_created_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 12, 44, 16, 596065, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 12, 44, 16, 596654, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]