# Generated by Django 4.1.7 on 2023-11-19 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addquestionblock',
            name='whatsapp_link',
            field=models.CharField(help_text='Используется в кнопке', max_length=255, verbose_name='Ссылка на Whatsapp'),
        ),
    ]