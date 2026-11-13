import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def env_list(name, default=''):
    """Список из переменной окружения через запятую, без пустых элементов и пробелов."""
    return [item.strip() for item in os.environ.get(name, default).split(',') if item.strip()]


def env_bool(name, default=False):
    return os.environ.get(name, str(default)) == 'True'


DEBUG = env_bool('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
# Старые ключи на время ротации: сессии и токены, подписанные ими, остаются валидными.
SECRET_KEY_FALLBACKS = env_list('SECRET_KEY_FALLBACKS')
ALLOWED_HOSTS = env_list('ALLOWED_HOSTS')

CSRF_TRUSTED_ORIGINS = env_list('CSRF_TRUSTED')

# По умолчанию CORS разрешён тем же доменам, что и CSRF (cubekazan.ru и www.cubekazan.ru).
CORS_ALLOWED_ORIGINS = env_list('CORS_ALLOWED_ORIGINS') or CSRF_TRUSTED_ORIGINS
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with', 'Access-Control-Allow-Origin', 'X-Signature']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'CONN_MAX_AGE': int(os.environ.get('DB_CONN_MAX_AGE', '60')),
        'CONN_HEALTH_CHECKS': True,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

HMAC_KEY = os.environ.get("HMAC_KEY")

# --- Почта: уведомления менеджеру о новых заказах ---
# Отправка через SMTP почтового сервиса (Яндекс: smtp.yandex.ru:465 по SSL, пароль приложения).
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.yandex.ru')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '465'))
EMAIL_USE_SSL = env_bool('EMAIL_USE_SSL', True)
EMAIL_USE_TLS = env_bool('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
# Заказ отправляется синхронно: без таймаута зависший SMTP держал бы ответ клиенту.
EMAIL_TIMEOUT = int(os.environ.get('EMAIL_TIMEOUT', '10'))
# Яндекс и Mail.ru отклоняют письма, у которых отправитель не совпадает с логином ящика.
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL') or EMAIL_HOST_USER
SERVER_EMAIL = DEFAULT_FROM_EMAIL
# Кому слать уведомления о заказах, через запятую.
ORDER_NOTIFY_EMAILS = env_list('ORDER_NOTIFY_EMAILS')
# Адрес сайта для ссылки на заказ в админке. По умолчанию первый из CSRF_TRUSTED.
SITE_URL = (os.environ.get('SITE_URL') or next(iter(CSRF_TRUSTED_ORIGINS), '')).rstrip('/')

# --- HTTPS и заголовки безопасности ---
# TLS завершается на nginx хоста, который передаёт X-Forwarded-Proto: https.
# Внутренний nginx (Dockerfile.frontend) пробрасывает этот заголовок как есть.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env_bool('SECURE_SSL_REDIRECT', True)
# Docker healthcheck ходит внутрь контейнера по http — его не редиректим.
SECURE_REDIRECT_EXEMPT = [r'^healthcheck/$']
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', '0'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = env_bool('SECURE_HSTS_INCLUDE_SUBDOMAINS')
SECURE_HSTS_PRELOAD = env_bool('SECURE_HSTS_PRELOAD')
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = env_bool('CSRF_COOKIE_SECURE')
SESSION_COOKIE_SECURE = env_bool('SESSION_COOKIE_SECURE')
SESSION_COOKIE_HTTPONLY = True

# Осознанно принятые предупреждения `manage.py check`, через запятую,
# например: ckeditor.W001,security.W005,security.W021
SILENCED_SYSTEM_CHECKS = env_list('SILENCED_SYSTEM_CHECKS')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': os.environ.get('LOG_LEVEL', 'WARNING')},
    # Письма о заказах: INFO, чтобы в логах было видно, что уведомление ушло.
    'loggers': {'shop': {'handlers': ['console'], 'level': 'INFO', 'propagate': False}},
}
