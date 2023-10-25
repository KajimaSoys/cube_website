from django.db import models
from django.utils import timezone
from datetime import datetime


def default_date():
    return datetime.now()


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', help_text='не больше 50 символов', blank=False)
    text = models.TextField(verbose_name='Содержание', blank=False)
    published = models.BooleanField(verbose_name='Опубликовать', default=False)
    image = models.ImageField(verbose_name='Изображение', upload_to='shop/news')
    created = models.DateTimeField(verbose_name='Дата создания', default=default_date)
    slug = models.SlugField(verbose_name='Транслитерация', help_text='Заполняется автоматически')

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Reviews(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=40, blank=False)
    reviews = models.TextField(verbose_name='Отзыв', blank=False)
    date = models.DateTimeField(verbose_name='Дата создания', default=default_date)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
