from django.db import models
from datetime import datetime
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField


def default_date():
    return datetime.now()


class Reviews(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=100)
    review = RichTextField(verbose_name='Текста отзыва')

    image = ResizedImageField(
        upload_to='service/reviews',
        verbose_name='Оригинал отзыва',
        quality=85,
    )

    creation_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    published = models.BooleanField(verbose_name='Опубликовано?', default=True)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок")

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ('order', )

    def __str__(self):
        return self.name
