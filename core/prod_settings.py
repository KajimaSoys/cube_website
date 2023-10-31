import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = (os.environ.get('DEBUG') == 'True')
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED")]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",# from nginx in prod
]


CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with', 'Access-Control-Allow-Origin', 'X-Signature']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': os.environ.get('DB_PORT'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, "static/")


CSRF_COOKIE_SECURE = (os.environ.get('CSRF_COOKIE_SECURE', False) == 'True')
SESSION_COOKIE_SECURE = (os.environ.get('SESSION_COOKIE_SECURE', False) == 'True')

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/home/kajimasoys/website/cache'
#     }
# }

