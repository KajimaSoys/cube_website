# Generated by Django 4.1.7 on 2023-11-19 01:44

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('common_elements', '0002_alter_addquestionblock_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addquestionblock',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=80, scale=None, size=[1260, None], upload_to='common_elements/add_question/', verbose_name='Фото'),
        ),
    ]
