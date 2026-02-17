from django.db import models
from ckeditor.fields import RichTextField
from shop.models import Product


class MainBlock(models.Model):
    """
    Description of MainBlock Model of Main Page App.

    Fields:
    - company_name: Name of the company;
    - title: Title;
    - description: Description;
    - bar_first: First card;
    - bar_second: Second card;
    - bar_third: Third card;
    - bar_fourth: Fourth card;
    - image: Image.
    """

    company_name = models.CharField(verbose_name='Название компании', max_length=250)
    title = RichTextField(verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    bar_first = models.CharField(verbose_name='Карточка №1', max_length=250)
    bar_second = models.CharField(verbose_name='Карточка №2', max_length=250)
    bar_third = models.CharField(verbose_name='Карточка №3', max_length=250)
    bar_fourth = models.CharField(verbose_name='Карточка №4', max_length=250)

    image = models.FileField(verbose_name='Фото', upload_to='main_page/main/', max_length=500)

    def __str__(self):
        return 'Главный блок'

    class Meta:
        verbose_name = '1 - Главный блок'
        verbose_name_plural = '1 - Главный блок'


class CatalogTeaserBlock(models.Model):
    """
    Description of CatalogTeaserBlock Model of Main Page App.

    Fields:
    - title: Title.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)

    def __str__(self):
        return 'Тизер  каталога'

    class Meta:
        verbose_name = '2 - Тизер каталога'
        verbose_name_plural = '2 - Тизер каталога'


class ServiceOptionsBlock(models.Model):
    """
    Description of ServiceOptionsBlock Model of Main Page App.

    Fields:
    - title: Title;
    - option_first: First text;
    - image_first: First image;
    - option_second: Second text;
    - image_second: Second image;
    - option_third: Third text;
    - image_third: Third image.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)

    option_first = models.CharField(verbose_name='Текст', max_length=50)
    image_first = models.FileField(verbose_name='Фото', upload_to='main_page/service_options/', max_length=500)

    option_second = models.CharField(verbose_name='Текст', max_length=50)
    image_second = models.FileField(verbose_name='Фото', upload_to='main_page/service_options/', max_length=500)

    option_third = models.CharField(verbose_name='Текст', max_length=50)
    image_third = models.FileField(verbose_name='Фото', upload_to='main_page/service_options/', max_length=500)

    def __str__(self):
        return 'Услуги компании'

    class Meta:
        verbose_name = '3 - Услуги компании'
        verbose_name_plural = '3 - Услуги компании'


class CalculatorBlock(models.Model):
    """
    Description of CalculatorBlock Model of Main Page App.

    Fields:
    - title: Title;
    - description: Description;
    - image: Image.
    """

    title = RichTextField(verbose_name='Заголовок')
    description = models.CharField(verbose_name='Описание', max_length=500)

    image = models.FileField(verbose_name='Фото', upload_to='main_page/calculator/', max_length=500)

    def __str__(self):
        return 'Блок калькулятора'

    class Meta:
        verbose_name = '4 - Блок калькулятора'
        verbose_name_plural = '4 - Блок калькулятора'


class NewProductBlock(models.Model):
    """
    Description of NewProductBlock Model of Main Page App.

    Fields:
    - order: Order of the product;
    - product: Product.
    """

    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Товар")

    def __str__(self):
        return self.product.name if self.product else 'Удалённый товар'

    class Meta:
        verbose_name = 'новинка'
        verbose_name_plural = '5 - Новинки'
        ordering = ['order', ]


class PopularProductBlock(models.Model):
    """
    Description of PopularProductBlock Model of Main Page App.

    Fields:
    - order: Order of the product;
    - product: Product.
    """

    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Товар")

    def __str__(self):
        return self.product.name if self.product else 'Удалённый товар'

    class Meta:
        verbose_name = 'популярная модель'
        verbose_name_plural = '6 - Популярные модели'
        ordering = ['order', ]


class DeliveryBlock(models.Model):
    """
    Description of DeliveryBlock Model of Main Page App.

    Fields:
    - title: Title;
    - subtitle_first: First subtitle;
    - text_first: First description;
    - additional_first: Additional first text;
    - image_first: First image;
    - subtitle_second: Second subtitle;
    - text_second: Second description;
    - additional_second: Additional second text;
    - image_second: Second image.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=500)

    subtitle_first = models.CharField(verbose_name='Подзаголовок', max_length=500)
    text_first = models.CharField(verbose_name='Описание', max_length=500)
    additional_first = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)
    image_first = models.FileField(verbose_name='Фото', upload_to='main_page/delivery/', max_length=500)

    subtitle_second = models.CharField(verbose_name='Подзаголовок', max_length=500)
    text_second = models.CharField(verbose_name='Описание', max_length=500)
    additional_second = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)
    image_second = models.FileField(verbose_name='Фото', upload_to='main_page/delivery/', max_length=500)

    def __str__(self):
        return 'Доставка'

    class Meta:
        verbose_name = '7 - Доставка'
        verbose_name_plural = '7 - Доставка'


class AdvantagesBlock(models.Model):
    """
    Description of AdvantagesBlock Model of Main Page App.

    Fields:
    - title: Title;
    - subtitle_first: First subtitle;
    - text_first: First description;
    - additional_first: Additional first text;
    - subtitle_second: Second subtitle;
    - text_second: Second description;
    - additional_second: Additional second text;
    - subtitle_third: Third subtitle;
    - text_third: Third description;
    - additional_third: Additional third text;
    - subtitle_fourth: Fourth subtitle;
    - text_fourth: Fourth description;
    - additional_fourth: Additional fourth text;
    - subtitle_fifth: Fifth subtitle;
    - text_fifth: Fifth description;
    - additional_fifth: Additional fifth text;
    - subtitle_sixth: Sixth subtitle;
    - text_sixth: Sixth description;
    - additional_sixth: Additional sixth text.
    """

    title = RichTextField(verbose_name='Заголовок')

    subtitle_first = RichTextField(verbose_name='Подзаголовок')
    text_first = models.CharField(verbose_name='Описание', max_length=500)
    additional_first = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)

    subtitle_second = RichTextField(verbose_name='Подзаголовок')
    text_second = models.CharField(verbose_name='Описание', max_length=500)
    additional_second = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)

    subtitle_third = RichTextField(verbose_name='Подзаголовок')
    text_third = models.CharField(verbose_name='Описание', max_length=500)
    additional_third = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)

    subtitle_fourth = RichTextField(verbose_name='Подзаголовок')
    text_fourth = models.CharField(verbose_name='Описание', max_length=500)
    additional_fourth = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)

    subtitle_fifth = RichTextField(verbose_name='Подзаголовок')
    text_fifth = models.CharField(verbose_name='Описание', max_length=500)
    additional_fifth = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)

    subtitle_sixth = RichTextField(verbose_name='Подзаголовок')
    text_sixth = models.CharField(verbose_name='Описание', max_length=500)
    additional_sixth = models.CharField(verbose_name='Дополнительный текст', max_length=500, blank=True, null=True)

    def __str__(self):
        return 'Преимущества компании'

    class Meta:
        verbose_name = '8 - Преимущества компании'
        verbose_name_plural = '8 - Преимущества компании'


class CartonInfoBlock(models.Model):
    """
    Description of CartonInfoBlock Model of Main Page App.

    Fields:
    - title: Title;
    - description: Description;
    - quality_block: Quality text;
    - subtitle_first: First subtitle;
    - text_first: First description;
    - image_first: First image;
    - subtitle_second: Second subtitle;
    - text_second: Second description;
    - image_second: Second image.
    """

    title = RichTextField(verbose_name='Заголовок')
    description = models.CharField(verbose_name='Описание', max_length=500)
    quality_block = models.CharField(verbose_name='Текст о качестве', max_length=500)

    subtitle_first = models.CharField(verbose_name='Подзаголовок', max_length=500)
    text_first = models.CharField(verbose_name='Описание', max_length=500)
    image_first = models.FileField(verbose_name='Фото', upload_to='main_page/carton_info/', max_length=500)

    subtitle_second = models.CharField(verbose_name='Подзаголовок', max_length=500)
    text_second = models.CharField(verbose_name='Описание', max_length=500)
    image_second = models.FileField(verbose_name='Фото', upload_to='main_page/carton_info/', max_length=500)

    def __str__(self):
        return 'Информация о картоне'

    class Meta:
        verbose_name = '9 - Информация о картоне'
        verbose_name_plural = '9 - Информация о картоне'


class RequestBlock(models.Model):
    """
    Description of RequestBlock Model of Main Page App.

    Fields:
    - title: Title;
    - description: Description;
    - whatsapp_link: WhatsApp link;
    - image: Image.
    """

    title = RichTextField(verbose_name='Заголовок')
    description = models.CharField(verbose_name='Описание', max_length=500)
    whatsapp_link = models.CharField(verbose_name='Ссылка на Whatsapp', max_length=255,
                                     help_text='Используется в кнопке')

    image = models.FileField(verbose_name='Фото', upload_to='main_page/request/', max_length=500)

    def __str__(self):
        return 'Блок заявки в Whatsapp'

    class Meta:
        verbose_name = '10 - Блок заявки в Whatsapp'
        verbose_name_plural = '10 - Блок заявки в Whatsapp'


class QuestionsBlock(models.Model):
    """
    Description of QuestionsBlock Model of Main Page App.

    Fields:
    - question: Question;
    - answer: Answer;
    - order: Order of the question.
    """

    question = models.CharField(verbose_name='Вопрос', max_length=500)
    answer = RichTextField(verbose_name='Ответ')  # , config_name='default'

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Порядок'
    )

    def __str__(self):
        return 'Частые вопросы'

    class Meta:
        verbose_name = '11 - Частые вопросы'
        verbose_name_plural = '11 - Частые вопросы'
        ordering = ['order', ]


class ContactsBlock(models.Model):
    """
    Description of ContactsBlock Model of Main Page App.

    Fields:
    - title: Title;
    - tg_link: Telegram link;
    - whatsapp_link: WhatsApp link;
    - monday_friday_schedule: Schedule for Monday to Friday;
    - sunday_schedule: Schedule for Saturday;
    - dinner_schedule: Schedule for Sunday;
    - number: Phone number;
    - mail: Email address.
    """

    title = RichTextField(verbose_name='Заголовок')
    tg_link = models.CharField(verbose_name='Ссылка на Telegram', max_length=255)
    whatsapp_link = models.CharField(verbose_name='Ссылка на Whatsapp', max_length=255)

    monday_friday_schedule = models.CharField(verbose_name='Расписание (понедельник-пятница)', max_length=255, help_text='чч:мм-чч:мм')
    sunday_schedule = models.CharField(verbose_name='Расписание (суббота)', max_length=255, help_text='чч:мм-чч:мм')
    dinner_schedule = models.CharField(verbose_name='Расписание (воскресенье)', max_length=255, help_text='чч:мм-чч:мм')

    number = models.CharField(verbose_name='Номер телефона', max_length=255)
    mail = models.CharField(verbose_name='Почта', max_length=255)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = '12 - Контакты'
        verbose_name_plural = '12 - Контакты'
