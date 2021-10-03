from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1' , 'quizzbuddyy.herokuapp.com']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
