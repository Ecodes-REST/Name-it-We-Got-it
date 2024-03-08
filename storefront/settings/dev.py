from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT':'57126',
        'USER': 'postgres',
        'PASSWORD': 'JBSTofsnkyJgGMgOURAkQsdXgdXkgoQj'
    }
}

CELERY_BROKER_URL= 'redis://localhost:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525