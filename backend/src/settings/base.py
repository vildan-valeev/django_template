import redis
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool("DEBUG", False)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    "django_dramatiq",

    'shop.apps.ShopConfig',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# print(BASE_DIR)
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'  # сбор всей статики в одну директорию для вебсервера nginx
STATICFILES_DIRS = [
    "static",  # указываем где еще может находиться статика помимо app/static/app/css/example.css
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

CORS_ALLOW_ALL_ORIGINS = True

REDIS_HOST = env.str("REDIS_HOST", "localhost")

DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",
    "OPTIONS": {
        "url": f"redis://{REDIS_HOST}:6379/0",
    },
    "MIDDLEWARE": [
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Retries",
        "django_dramatiq.middleware.AdminMiddleware",
        "django_dramatiq.middleware.DbConnectionsMiddleware",
    ]
}
# DRAMATIQ_RESULT_BACKEND = {
#     "BACKEND": "dramatiq.results.backends.redis.RedisBackend",
#     "BACKEND_OPTIONS": {
#         "url": "redis://localhost:6379/0",
#     },
#     "MIDDLEWARE_OPTIONS": {
#         "result_ttl": 60000
#     }
# }
print(f'{DEBUG=}')
if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['tarataika.com'])

STATE = env.str('STATE')

print(f'{STATE} SETTINGS COMPLETE!!!')
