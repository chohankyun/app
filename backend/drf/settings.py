"""
Django settings for drf project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import datetime
import logging.config
import os
import sys
from pathlib import Path

import pymysql
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _

from backend.com.util.env import EnvJson

pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Logger
LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': "%Y/%b/%d %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': "midnight",
            'backupCount': 0,
            'encoding': 'utf-8',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'log/backend.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
        },
        'django.request': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'app': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOGGING)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = EnvJson.get('SECRET_KEY')
FIELD_ENCRYPTION_KEYS = EnvJson.get('FIELD_ENCRYPTION_KEYS')
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'rest_framework',
    'encrypted_fields',
    'backend.com.jwt.apps.JwtConfig',
    'backend.api.join.apps.JoinConfig',
    'backend.api.user.apps.UserConfig',
    'backend.api.board.apps.BoardConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'backend.com.jwt.middleware.JSONWebTokenMiddleware',
]

ROOT_URLCONF = 'drf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'drf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': EnvJson.get('DB_HOST'),
        'PORT': 3306,
        'NAME': 'app_db',
        'USER': 'app_user',
        'PASSWORD': EnvJson.get('DB_PASSWORD'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('ko', _('Korean')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locales"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/web/'

if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'web'),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'web')

# Auth User
AUTH_USER_MODEL = 'user.User'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'com.jwt.authentication.JSONWebTokenAuthentication',
    ],
}

JWT_AUTH = {
    'JWT_USER': 'backend.com.jwt.handler.User',
    'JWT_SALT': 'backend.com.jwt.handler.Salt',
}

# Message
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.ap-northeast-2.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'AKIATDLV5W7XPTHAF4UN'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = 'aws-lsg-billing@lsitc.com'
