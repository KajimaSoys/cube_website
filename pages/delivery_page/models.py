from django.db import models


class PaymentBlock(models.Model):
    """
    Description of PaymentBlock Model of Delivery Page App.

    Fields:
    - title: Title;
    - question_link: Chat link;
    - subtitle_first: First subtitle;
    - text_first: First description;
    - image_first: First image;
    - subtitle_second: Second subtitle;
    - text_second: Second description;
    - image_second: Second image.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    question_link = models.CharField(verbose_name='Ссылка на чат', max_length=500)

    subtitle_first = models.CharField(verbose_name='Подзаголовок', max_length=500)
    text_first = models.CharField(verbose_name='Описание', max_length=500)
    image_first = models.FileField(verbose_name='Фото', upload_to='delivery_page/payment/', max_length=500)

    subtitle_second = models.CharField(verbose_name='Подзаголовок', max_length=500)
    text_second = models.CharField(verbose_name='Описание', max_length=500)
    image_second = models.FileField(verbose_name='Фото', upload_to='delivery_page/payment/', max_length=500)

    def __str__(self):
        return 'Доставка'

    class Meta:
        verbose_name = '2 - Оплата'
        verbose_name_plural = '2 - Оплата'
