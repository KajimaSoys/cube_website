# Generated by Django 4.1.7 on 2024-01-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_alter_cartoninfoblock_image_first_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsblock',
            name='dinner_schedule',
            field=models.CharField(help_text='чч:мм-чч:мм', max_length=255, verbose_name='Расписание (воскресенье)'),
        ),
    ]
