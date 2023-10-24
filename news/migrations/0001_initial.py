# Generated by Django 4.1.7 on 2023-04-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='не больше 50 символов', max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('image', models.ImageField(upload_to='shop/news')),
            ],
        ),
    ]
