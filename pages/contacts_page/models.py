from django.db import models


class OutsideView(models.Model):
    """
    Description of OutsideView Model of Contacts Page App.

    Fields:
    - image_first: First image;
    - text_first: First description;
    - image_second: Second image;
    - text_second: Second description;
    - image_third: Third image;
    - text_third: Third description.
    """

    image_first = models.FileField(verbose_name='Фото', upload_to='contacts_page/outside_view/', max_length=500)
    text_first = models.CharField(verbose_name='Описание', max_length=500)

    image_second = models.FileField(verbose_name='Фото', upload_to='contacts_page/outside_view/', max_length=500)
    text_second = models.CharField(verbose_name='Описание', max_length=500)

    image_third = models.FileField(verbose_name='Фото', upload_to='contacts_page/outside_view/', max_length=500)
    text_third = models.CharField(verbose_name='Описание', max_length=500)

    def __str__(self):
        return 'Блок местонахождения компании'

    class Meta:
        verbose_name = '2 - Блок местонахождения компании'
        verbose_name_plural = '2 - Блок местонахождения компании'
