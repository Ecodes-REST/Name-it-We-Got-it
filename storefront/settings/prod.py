import os
import dj_database_url
from .common import *

DEBUG= False

SECRET_KEY= os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': dj_database_url.config()
}

REDIS= os.environ['REDIS_URL']

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


EMAIL_HOST = os.environ['*']
EMAIL_HOST_USER = os.environ['']
EMAIL_HOST_PASSWORD = os.environ[dj_database_url.config()]
EMAIL_PORT = 2525