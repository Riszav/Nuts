from pathlib import Path
from .jazzmin import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS
from .ckeditor import customColorPalette, CKEDITOR_5_CONFIGS, CKEDITOR_5_CUSTOM_CSS
from decouple import config
from .unfold import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
PROD = config("PROD", cast=bool)
if PROD:
    from .prod import *
else:
    from .dev import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    # "unfold.contrib.import_export",  # optional, if django-import-export package is used
    # "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'corsheaders',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_ckeditor_5',
    'drf_spectacular',
    'pytest',
    "debug_toolbar",

    'src.apps.nuts',
    'src.apps.news',
    'src.apps.generals',
    'src.apps.about_us',
    'django_seed'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    "127.0.0.1",
    "35.183.81.168",
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'config.pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d.%m.%Y %H:%M',
    'DATE_FORMAT': '%d.%m.%Y',
    'DEFAULT_TIME_FORMAT': '%H:%M',
    'DATETIME_INPUT_FORMATS': ('%d.%m.%Y %H:%M',),
    'DATE_INPUT_FORMATS': ('%d.%m.%Y',),
    'TIME_INPUT_FORMATS': ('%H:%M',),
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

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

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ru', 'en')

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True
USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

STATIC_URL = '/back_static/'
STATIC_ROOT = BASE_DIR / 'back_static'
STATICFILES_DIRS = [
    BASE_DIR / 'locale_static'
]

MEDIA_URL = '/back_media/'
MEDIA_ROOT = BASE_DIR / 'back_media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
#
# JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

customColorPalette = customColorPalette

CKEDITOR_5_CONFIGS = CKEDITOR_5_CONFIGS

CKEDITOR_5_CUSTOM_CSS = CKEDITOR_5_CUSTOM_CSS

MODELTRANSLATION_CUSTOM_FIELDS = ('CKEditor5Field', )

# CKEDITOR_5_FILE_STORAGE = CKEDITOR_5_FILE_STORAGE

SPECTACULAR_SETTINGS = {
    'TITLE': 'SOLAAR`s API',
    'DESCRIPTION': 'Тут продаются лучше орехи во всем диком западе',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'displayOperationId': True,
    },
}

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8000',
#     'http://127.0.0.1:8000',
# ]
#
# CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']

X_FRAME_OPTIONS = 'SAMEORIGIN'
