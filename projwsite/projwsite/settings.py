
VIRTUAL_ENV="/Users/ENGINE/src/ALL_PROJ/2website_aff/env"


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projwsite.settings")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')mf15d$6h)o0*e-$&wf9!*%2#d*3yekv(x9qgph!*q&&p_dxjl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =   True   #  False #   False for PRODUCTION

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aff',
    'django_extensions',
    'crispy_forms',
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

ROOT_URLCONF = 'projwsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'projwsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dbmasteruser',
#         'USER': 'dbmasteruser',
#         'PASSWORD': '($1S2NhT~gRv.hXMlAQj9n]kj]<,)K#6',
#         'HOST': 'ls-652f5476a10cea2009615c8a44e34c588c9cffe1.c1sebzs839ys.us-west-2.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# }
# run migrations on new server 

DEFAULT_FROM_EMAIL = 'voxvictoria@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/aff/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'aff/static/'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
