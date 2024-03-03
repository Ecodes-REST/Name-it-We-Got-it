import os
import dj_database_url
from .common import *

DEBUG= False

SECRET_KEY= os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': dj_database_url.config()
}

REDIS_URL= os.environ.get('REDIS_URL')

CELERY_BROKER_URL= REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 2525)