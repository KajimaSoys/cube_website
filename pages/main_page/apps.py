from django.apps import AppConfig


class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages.main_page'
    verbose_name = 'Наполнение сайта - Главная страница'
