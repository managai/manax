# -*- coding: utf-8 -*-
import os
from .common import *

# load env variables from env.dreamhost
env.read_env(str(ROOT_DIR) + '/env.dreamhost')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = os.path.dirname(ROOT_DIR) + '/../public/static/'

SECRET_KEY = 'o}ljke~Rrgg@yGwVIJf~k.(<5E+=5b|0=@(Gb=cO9%Fj~5wi4z'

ALLOWED_HOSTS = ['{{ cookiecutter.domain_name }}']

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db('DATABASE_URL')
