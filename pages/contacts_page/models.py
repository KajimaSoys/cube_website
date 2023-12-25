from django.db import models
from django_resized import ResizedImageField


class OutsideView(models.Model):
    """
    Description of OutsideView Model of Contacts Page App
    """
    image_first = models.FileField(verbose_name='Фото', upload_to='contacts_page/outside_view/', max_length=500)
    # image_first = ResizedImageField(upload_to='contacts_page/outside_view/',
    #                                 verbose_name='Фото',
    #                                 size=[610, None],
    #                                 quality=80, )
    text_first = models.CharField(verbose_name='Описание', max_length=500)

    image_second = models.FileField(verbose_name='Фото', upload_to='contacts_page/outside_view/', max_length=500)
    # image_second = ResizedImageField(upload_to='contacts_page/outside_view/',
    #                                  verbose_name='Фото',
    #                                  size=[610, None],
    #                                  quality=80, )
    text_second = models.CharField(verbose_name='Описание', max_length=500)

    image_third = models.FileField(verbose_name='Фото', upload_to='contacts_page/outside_view/', max_length=500)
    # image_third = ResizedImageField(upload_to='contacts_page/outside_view/',
    #                                 verbose_name='Фото',
    #                                 size=[610, None],
    #                                 quality=80, )
    text_third = models.CharField(verbose_name='Описание', max_length=500)

    def __str__(self):
        return 'Блок местонахождения компании'

    class Meta:
        verbose_name = '2 - Блок местонахождения компании'
        verbose_name_plural = '2 - Блок местонахождения компании'
