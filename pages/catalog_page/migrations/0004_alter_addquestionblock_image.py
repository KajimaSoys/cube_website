# Generated by Django 4.1.7 on 2023-12-25 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_page', '0003_alter_addquestionblock_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addquestionblock',
            name='image',
            field=models.FileField(max_length=500, upload_to='catalog_page/add_question/', verbose_name='Фото'),
        ),
    ]
