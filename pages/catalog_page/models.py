from django.db import models
from django_resized import ResizedImageField


class AddQuestionBlock(models.Model):
    """
    Description of AddQuestionBlock Model of Catalog Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.CharField(verbose_name='Описание', max_length=500)
    whatsapp_link = models.CharField(verbose_name='Ссылка на Whatsapp', max_length=255,
                                     help_text='Используется в кнопке')

    image = models.FileField(verbose_name='Фото', upload_to='catalog_page/add_question/', max_length=500)
    # image = ResizedImageField(upload_to='catalog_page/add_question/',
    #                           verbose_name='Фото',
    #                           size=[1100, None],
    #                           quality=80, )

    def __str__(self):
        return 'Блок "Не нашли нужный размер?"'

    class Meta:
        verbose_name = '1 - Блок "Не нашли нужный размер?"'
        verbose_name_plural = '1 - Блок "Не нашли нужный размер?"'
