from django.db import models
from shop.models import Product
from django_resized import ResizedImageField


class HeaderBlock(models.Model):
    """
    Description of HeaderBlock Model of Common Elements App
    """

    logo = models.FileField(verbose_name='Логотип', upload_to='common_elements/header/', max_length=500)

    number = models.CharField(verbose_name='Номер компании', max_length=255)
    mail = models.CharField(verbose_name='Почта', max_length=255, help_text='Используется в футере')
    address = models.CharField(verbose_name='Адрес компании', max_length=255)
    yandex_map_link = models.CharField(verbose_name='Ссылка на Яндекс Карты', max_length=500, default='')

    tg_link = models.CharField(verbose_name='Ссылка на Telegram', max_length=255, help_text='Используется в футере')
    whatsapp_link = models.CharField(verbose_name='Ссылка на Whatsapp', max_length=255, help_text='Используется в футере')

    def __str__(self):
        return 'Навигационная панель'

    class Meta:
        verbose_name = '1 - Навигационная панель и футер'
        verbose_name_plural = '1 - Навигационная панель и футер (Все страницы)'


class RecommendedProductBlock(models.Model):
    """
    Description of RecommendedProductBlock Model of Common Elements App
    """

    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Товар")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = '2 - Рекомендуемые товары'
        verbose_name_plural = '2 - Рекомендуемые товары (Страницы товара, доставки, отзывов)'
        ordering = ['order', ]


class AddQuestionBlock(models.Model):
    """
    Description of AddQuestionBlock Model of Common Elements App
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)
    description = models.CharField(verbose_name='Описание', max_length=500)
    whatsapp_link = models.CharField(verbose_name='Ссылка на Whatsapp', max_length=255,
                                     help_text='Используется в кнопке')

    image = models.FileField(verbose_name='Фото', upload_to='common_elements/add_question/', max_length=500)
    # image = ResizedImageField(upload_to='common_elements/add_question/',
    #                           verbose_name='Фото',
    #                           size=[1100, None],
    #                           quality=80, )

    def __str__(self):
        return 'Блок "Остались вопросы?"'

    class Meta:
        verbose_name = '3 - Блок "Остались вопросы?"'
        verbose_name_plural = '3 - Блок "Остались вопросы?" (Главная, страницы доставки, контактов, о компании, отзывов)'
