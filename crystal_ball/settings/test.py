"""
This is an example settings/test.py file.
Use this settings file when running tests.
These settings overrides what's in settings/base.py
"""

from .base import *


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '',
    },
}

SECRET_KEY = 'z^6mzx&6vh8a)ra8^rzt1e91vbnaon9(%n9=k$94!sb0xxmmuk'
