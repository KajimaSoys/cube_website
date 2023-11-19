from django.db import models


class AddQuestionBlock(models.Model):
    """
    Description of AddQuestionBlock Model of Catalog Page App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.CharField(verbose_name='Описание', max_length=500)
    whatsapp_link = models.CharField(verbose_name='ссылка на Whatsapp', max_length=255,
                                     help_text='Используется в кнопке')

    image = models.FileField(verbose_name='Фото', upload_to='catalog_page/add_question/', max_length=500)

    def __str__(self):
        return 'Блок "Не нашли нужный размер?"'

    class Meta:
        verbose_name = '1 - Блок "Не нашли нужный размер?"'
        verbose_name_plural = '1 - Блок "Не нашли нужный размер?"'
