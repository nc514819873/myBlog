from .base import * # NOQA

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'nc940306@',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}