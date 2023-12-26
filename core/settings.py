import os
from pathlib import Path

# app-model ordering imports
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

BASE_DIR = Path(__file__).resolve().parent.parent
USE_DJANGO_JQUERY = True

INSTALLED_APPS = [
    # project apps
    'shop.apps.ShopConfig',
    'news.apps.NewsConfig',
    'pages.common_elements.apps.CommonElementsConfig',
    'pages.main_page.apps.MainPageConfig',
    'pages.catalog_page.apps.CatalogPageConfig',
    'pages.product_page.apps.ProductPageConfig',
    'pages.delivery_page.apps.DeliveryPageConfig',
    'pages.contacts_page.apps.ContactsPageConfig',
    'pages.about_page.apps.AboutPageConfig',
    'pages.reviews_page.apps.ReviewsPageConfig',

    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd parties
    'debug_toolbar',
    'ckeditor',
    'rest_framework',
    'phone_field',
    'adminsortable2',
    'imagekit',
    'corsheaders',
]

MIDDLEWARE = [
    # default
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 3rd parties
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.DjangoModelPermissions'
    ]
}

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = "uploads/"

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *


# app-model ordering

ADMIN_ORDERING = (
    ('shop', ('Category', 'Product', 'Orders')),
    ('news', ('News', 'Reviews')),
    (
        'common_elements',
        (
            'HeaderBlock',
            'RecommendedProductBlock',
            'AddQuestionBlock'
        )
    ),
    (
        'main_page',
        (
            'MainBlock',
            'CatalogTeaserBlock',
            'ServiceOptionsBlock',
            'NewProductBlock',
            'PopularProductBlock',
            'DeliveryBlock',
            'AdvantagesBlock',
            'CartonInfoBlock',
            'RequestBlock',
            'QuestionsBlock',
            'ContactsBlock',
            'AddQuestionBlock'
        )
    ),
    (
        'catalog_page',
        (
            'AddQuestionBlock',
        )
    ),
    (
        'product_page',
        (
            'RecommendedProductBlock',
        )
    ),
    (
        'delivery_page',
        (
            'DeliveryBlock',
            'PaymentBlock',
            'RecommendedProductBlock',
            'AddQuestionBlock',
        )
    ),
    (
        'contacts_page',
        (
            'ContactsBlock',
            'OutsideView',
            'AddQuestionBlock',
        )
    ),
    (
        'about_page',
        (
            'AdvantagesBlock',
            'ServiceOptionsBlock',
            'CartonInfoBlock',
            'ContactsBlock',
            'OutsideView',
            'AddQuestionBlock',
        )
    ),
    (
        'reviews_page',
        (
            'RecommendedProductBlock',
            'AddQuestionBlock',
        )
    ),
    ('auth', ('User', 'Group')),
)

LINKED_MODELS = [
    # main_page
    {
        'source_app': 'common_elements',
        'target_app': 'main_page',
        'model_name': 'AddQuestionBlock',
        'model_name_verbose': '12 - Блок "Остались вопросы?"'
    },

    # product_page
    {
        'source_app': 'common_elements',
        'target_app': 'product_page',
        'model_name': 'RecommendedProductBlock',
        'model_name_verbose': '1 - Рекомендуемые товары'
    },

    # delivery_page
    {
        'source_app': 'main_page',
        'target_app': 'delivery_page',
        'model_name': 'DeliveryBlock',
        'model_name_verbose': '1 - Доставка'
    },
    {
        'source_app': 'common_elements',
        'target_app': 'delivery_page',
        'model_name': 'RecommendedProductBlock',
        'model_name_verbose': '3 - Рекомендуемые товары'
    },
    {
        'source_app': 'common_elements',
        'target_app': 'delivery_page',
        'model_name': 'AddQuestionBlock',
        'model_name_verbose': '4 - Блок "Остались вопросы?"'
    },

    # contacts_page
    {
        'source_app': 'main_page',
        'target_app': 'contacts_page',
        'model_name': 'ContactsBlock',
        'model_name_verbose': '1 - Контакты'
    },
    {
        'source_app': 'common_elements',
        'target_app': 'contacts_page',
        'model_name': 'AddQuestionBlock',
        'model_name_verbose': '3 - Блок "Остались вопросы?"'
    },

    # about_page
    {
        'source_app': 'main_page',
        'target_app': 'about_page',
        'model_name': 'AdvantagesBlock',
        'model_name_verbose': '1 - Преимущества компании'
    },
    {
        'source_app': 'main_page',
        'target_app': 'about_page',
        'model_name': 'ServiceOptionsBlock',
        'model_name_verbose': '2 - Услуги компании'
    },
    {
        'source_app': 'main_page',
        'target_app': 'about_page',
        'model_name': 'CartonInfoBlock',
        'model_name_verbose': '3 - Информация о картоне'
    },
    {
        'source_app': 'main_page',
        'target_app': 'about_page',
        'model_name': 'ContactsBlock',
        'model_name_verbose': '4 - Контакты'
    },
    {
        'source_app': 'contacts_page',
        'target_app': 'about_page',
        'model_name': 'OutsideView',
        'model_name_verbose': '5 - Блок местонахождения компании'
    },
    {
        'source_app': 'common_elements',
        'target_app': 'about_page',
        'model_name': 'AddQuestionBlock',
        'model_name_verbose': '6 - Блок "Остались вопросы?"'
    },

    # reviews_page
    {
        'source_app': 'common_elements',
        'target_app': 'reviews_page',
        'model_name': 'RecommendedProductBlock',
        'model_name_verbose': '1 - Рекомендуемые товары'
    },
    {
        'source_app': 'common_elements',
        'target_app': 'reviews_page',
        'model_name': 'AddQuestionBlock',
        'model_name_verbose': '2 - Блок "Остались вопросы?"'
    },
]


def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)

    if not app_dict:
        return

    NEW_ADMIN_ORDERING = []
    if app_label:
        for ao in ADMIN_ORDERING:
            if ao[0] == app_label:
                NEW_ADMIN_ORDERING.append(ao)
                break

    if not app_label:
        for app_key in list(app_dict.keys()):
            if not any(app_key in ao_app for ao_app in ADMIN_ORDERING):
                app_dict.pop(app_key)

    app_list = sorted(
        app_dict.values(),
        key=lambda x: [ao[0] for ao in ADMIN_ORDERING].index(x['app_label'])
    )

    # Обработка моделей и моделей-ссылок
    # print(f"target_app:\t{link['target_app']}\tapp_label:\t{app['app_label']}")

    for app in app_list:
        if app['app_label'] in [ao[0] for ao in ADMIN_ORDERING]:
            ao_models = next(ao[1] for ao in ADMIN_ORDERING if ao[0] == app['app_label'])
            updated_models = []

            for model_name in ao_models:
                # Добавляем оригинальные модели
                model = next((m for m in app['models'] if m['object_name'] == model_name), None)
                if model:
                    updated_models.append(model)

                # Добавляем модели-ссылки, если они есть
                link = next((link for link in LINKED_MODELS if
                             link['model_name'] == model_name and link['target_app'] == app['app_label']), None)
                if link:
                    model_url = reverse(f'admin:{link["source_app"].lower()}_{model_name.lower()}_changelist')
                    add_url = reverse(f'admin:{link["source_app"].lower()}_{model_name.lower()}_add')
                    updated_models.append({
                        'name': format_html('<a href="{}">{}</a>', model_url, link['model_name_verbose']),
                        'object_name': f'{model_name}Link',
                        'admin_url': model_url,
                        'add_url': add_url,
                    })

            app['models'] = updated_models

    return app_list


admin.AdminSite.get_app_list = get_app_list



