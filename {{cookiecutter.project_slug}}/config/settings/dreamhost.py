# -*- coding: utf-8 -*-
omport os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = os.path.dirname(ROOT_DIR) + '/../public/static/'

SECRET_KEY = 'o}ljke~Rrgg@yGwVIJf~k.(<5E+=5b|0=@(Gb=cO9%Fj~5wi4z'

ALLOWED_HOSTS = ['']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'osefveni',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

