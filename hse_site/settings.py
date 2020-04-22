"""
Django settings for hse_location project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', "tr01t%a68+1z_m+-zbsth)%xqu7bi&!b1yg&zsredfc*(g5-2t")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = []

ADMINS = (
    ("Francisc Furdui", "francisc.furdui2@mail.dcu.ie"),
)

MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "events.apps.EventsConfig",
    "theme.apps.ThemeConfig",
    "tailwind",
    "crispy_forms",
    "whitenoise.runserver_nostatic",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"
TAILWIND_APP_NAME = "theme"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hse_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

WSGI_APPLICATION = "hse_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static/"),
    os.path.join(
        BASE_DIR, "static/hse_site/"
    ),  # this is for static/hse_site/main.css
)

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Activate Django-Heroku.
django_heroku.settings(locals())
