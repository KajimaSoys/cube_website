import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
USE_DJANGO_JQUERY = True

INSTALLED_APPS = [
    # project apps
    'shop.apps.ShopConfig',
    'news.apps.NewsConfig',
    'pages.common_elements.apps.CommonElementsConfig',
    'pages.main_page.apps.MainPageConfig',
    'pages.catalog_page.apps.CatalogPageConfig',
    'pages.delivery_page.apps.DeliveryPageConfig',

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
    # 'corsheaders',
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
    # 'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.DjangoModelPermissions'
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
        )
    ),
    (
        'catalog_page',
        (
            'AddQuestionBlock',
        )
    ),
    (
        'delivery_page',
        (
            'Payment',
        )
    ),
    ('auth', ('User', 'Group')),
)

from django.contrib import admin


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

    for app, ao in zip(app_list, NEW_ADMIN_ORDERING or ADMIN_ORDERING):
        if app['app_label'] == ao[0]:
            for model in list(app['models']):
                if not model['object_name'] in ao[1]:
                    app['models'].remove(model)
        app['models'].sort(key=lambda x: ao[1].index(x['object_name']))
    return app_list


admin.AdminSite.get_app_list = get_app_list



