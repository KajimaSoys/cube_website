# Generated by Django 4.1.7 on 2023-11-19 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_elements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addquestionblock',
            options={'verbose_name': '3 - Блок "Остались вопросы?"', 'verbose_name_plural': '3 - Блок "Остались вопросы?" (Главная, страницы доставки, контактов, о компании, отзывов)'},
        ),
        migrations.AlterModelOptions(
            name='headerblock',
            options={'verbose_name': '1 - Навигационная панель и футер', 'verbose_name_plural': '1 - Навигационная панель и футер (Все страницы)'},
        ),
        migrations.AlterModelOptions(
            name='recommendedproductblock',
            options={'ordering': ['order'], 'verbose_name': '2 - Рекомендуемые товары', 'verbose_name_plural': '2 - Рекомендуемые товары (Страницы товара, доставки, отзывов)'},
        ),
        migrations.AddField(
            model_name='addquestionblock',
            name='whatsapp_link',
            field=models.CharField(default='', help_text='Используется в кнопке', max_length=255, verbose_name='Ссылка на Whatsapp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='tg_link',
            field=models.CharField(help_text='Используется в футере', max_length=255, verbose_name='Ссылка на Telegram'),
        ),
    ]
