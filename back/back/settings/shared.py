"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

# reading .env file
env = environ.Env()
environ.Env.read_env()

GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
    "output": "project_visualized.png",
    "pydot": True,
}

# Build paths inside the project like this: BASE_DIR / ...
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start settings
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Secret key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")


# Allowed hosts
# SECURITY WARNING: use only the server name, not *!
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Site Config
SITE_ID = int(env("SITE_ID", default="1"))

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
EMAIL_USE_TLS = not EMAIL_USE_SSL
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
OTP_EMAIL_SENDER = EMAIL_HOST_USER
OTP_EMAIL_TOKEN_VALIDITY = 300

# Phone settings
PHONENUMBER_DEFAULT_REGION = env("PHONENUMBER_DEFAULT_REGION")

# simple-mail settings
# https://github.com/VingtCinq/django-simple-mail
SIMPLE_MAIL_USE_CKEDITOR = True

# Application definition
# fmt: off
INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',  # enable search

    # our apps
    'back.apps.user.apps.UserConfig',
    'back.apps.social.apps.SocialConfig',
    'back.apps.address.apps.AddressConfig',
    'back.apps.client.apps.ClientConfig',
    'back.apps.business.apps.BusinessConfig',
    'back.apps.post.apps.PostConfig',
    'back.apps.vehicle.apps.VehicleConfig',
    'back.apps.job.apps.JobConfig',
    'back.apps.service.apps.ServiceConfig',
    'back.apps.media.apps.MediaConfig',
    'back.apps.about.apps.AboutConfig',

    ## 3rd parties ##
    'django_filters',
    'rest_framework',

    # jwt
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist', # token black listing

    # otp
    'django_otp',
    'django_otp.plugins.otp_email',

    # api documentation
    'drf_spectacular',

    # email
    'simple_mail',
    'ckeditor',

    # cors
    "corsheaders",

    #exts
    'django_extensions',
]
# fmt: on

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(BASE_DIR / "templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

WSGI_APPLICATION = "back.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Caracas"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = [
    str(BASE_DIR / "static"),
]
STATIC_ROOT = str(BASE_DIR / "../static")
MEDIA_URL = "media/"
MEDIA_ROOT = str(BASE_DIR / "../media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom AUTH Backend
AUTHENTICATION_BACKENDS = ['back.core.backends.UsernameOrEmailModelBackend']

# RestFramework settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "PAGE_SIZE": 10,
    # "NON_FIELD_ERRORS_KEY": "general_error",
    "EXCEPTION_HANDLER": "back.core.exception_handler.default_handler",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "DEGVABank API",
    "DESCRIPTION": "Bank for all of you",
    "VERSION": "1.0.0",
}


# Specifing our user
AUTH_USER_MODEL = "user.User"  # Currently not using it


# DRF simplejwt settings
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
REFRESH_TOKEN_LIFETIME = timedelta(days=1)
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": REFRESH_TOKEN_LIFETIME,
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# Expect https from HTTP Server
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# CORS settings
# https://github.com/adamchainz/django-cors-headers
# TODO: REMOVE LOCALHOST ONES WHEN IT IS IN REAL PRODUCTION
CORS_ALLOWED_ORIGINS = [
    "https://api.ati2.vittorioadesso.com",
    "https://ait2.vittorioadesso.com",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CSRF_TRUSTED_ORIGINS = [
    "https://api.ati2.vittorioadesso.com",
    "https://ait2.vittorioadesso.com",
]

CORS_ALLOW_CREDENTIALS = True
