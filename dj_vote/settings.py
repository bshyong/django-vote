# """
# Django settings for dj_vote project.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.6/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.6/ref/settings/
# """

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'dxxayo7bhk2ui3)w(j#0u8ajwyw*o2$93j&1r%b*w!gt2lr0%d'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# TEMPLATE_DEBUG = True

# # Allow all host headers
# ALLOWED_HOSTS = ['*']

# # Application definition

# INSTALLED_APPS = (
#   'django.contrib.admin',
#   'django.contrib.auth',
#   'django.contrib.contenttypes',
#   'django.contrib.sessions',
#   'django.contrib.messages',
#   'django.contrib.staticfiles',
# )

# MIDDLEWARE_CLASSES = (
#   'django.contrib.sessions.middleware.SessionMiddleware',
#   'django.middleware.common.CommonMiddleware',
#   'django.middleware.csrf.CsrfViewMiddleware',
#   'django.contrib.auth.middleware.AuthenticationMiddleware',
#   'django.contrib.messages.middleware.MessageMiddleware',
#   'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )

# ROOT_URLCONF = 'dj_vote.urls'

# WSGI_APPLICATION = 'dj_vote.wsgi.application'

# # Database
# # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# #     }
# # }

# # Internationalization
# # https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'EST'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#   os.path.join(BASE_DIR, 'static'),
# )

# # Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] = dj_database_url.config()

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ---

# -*- coding: utf-8 -*-
import os
import dj_database_url

boolean = lambda value: bool(int(value))
local_path = lambda path: os.path.join(os.path.dirname(__file__), path)

DEBUG = boolean(os.environ.get('DEBUG', 0))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'EST'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', local_path('media/'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.environ.get('STATIC_ROOT', local_path('static/'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

# Additional locations of static files
STATICFILES_DIRS = []

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{secret_key}}'

# List of callables that know how to import templates from various sources.
if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
else:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    local_path('templates/')
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.admin',
  'gunicorn',
  'raven.contrib.django',
  'south'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


