"""
Django settings for BigDjango project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cogyon4=aw0*u=@u8$==jb70p#ce!1*@7ee+js*+(b@0_mwkrn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_beat',  # django celery定时相关组件
    'django_celery_results',  # django celery执行结果存储组件

    'widget_tweaks',  # 用户美化表单
    'django_filters',  # 自定义过滤字段
    'django_tables2',  # 自定义表格显示字段

    # apps
    'apps.rbac',
    'apps.users',

    'import_export'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BigDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 在模板里面可以直接使用settings的DEBUG参数以及强大的sql_queries:它本身是一个字典，其中包括当前页面执行SQL查询所需的时间
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # 在模板中可以直接使用request对象
                'django.contrib.auth.context_processors.auth',  # 在模板里面可以直接使用user，perms对象。
                'django.contrib.messages.context_processors.messages',  # 在模板里面可以直接使用message对象。

                # 另外Django还提供了几个全局上下文处理器：
                # django.template.context_processors.i18n：在模板里面可以直接使用settings的LANGUAGES和LANGUAGE_CODE
                # django.template.context_processors.media：可以在模板里面使用settings的MEDIA_URL参数
                # django.template.context_processors.csrf : 给模板标签 csrf_token提供值
                # django.template.context_processors.tz: 可以在模板里面使用 TIME_ZONE参数。

                # 自定义全局上下文处理器
                # 'BigDjango..global_site_name',  # 全局设置网站名
            ],
        },
    },
]

WSGI_APPLICATION = 'BigDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.dirname(os.path.abspath(__file__)) + '/mysql.cnf'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'
SIMPLEUI_LOGO = 'https://th.bing.com/th/id/R2411a2b340731d67dfa0d84503e915e3?rik=zmYce%2fLys72JVQ&pid=ImgRaw'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
AUTH_USER_MODEL = 'rbac.UserProfile'

SITE_NAME = 'Sophomore'
