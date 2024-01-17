# Generated by Django 4.1.7 on 2024-01-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutsideView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_first', models.FileField(max_length=500, upload_to='contacts_page/outside_view/', verbose_name='Фото')),
                ('text_first', models.CharField(max_length=500, verbose_name='Описание')),
                ('image_second', models.FileField(max_length=500, upload_to='contacts_page/outside_view/', verbose_name='Фото')),
                ('text_second', models.CharField(max_length=500, verbose_name='Описание')),
                ('image_third', models.FileField(max_length=500, upload_to='contacts_page/outside_view/', verbose_name='Фото')),
                ('text_third', models.CharField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '2 - Блок местонахождения компании',
                'verbose_name_plural': '2 - Блок местонахождения компании',
            },
        ),
    ]
