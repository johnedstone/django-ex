import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The SECRET_KEY is provided via an environment variable in OpenShift
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    # safe value used for development when DJANGO_SECRET_KEY might not be set
    '9e4@&tw46$l31)zrqe3wi+-slqm(ruvz&se0^%9#6(_w3ui!c0'
)
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    #'feedback',
    'welcome',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # use whitenoise in prd
    # http://whitenoise.evans.io/en/latest/django.html
    #'whitenoise.middleware.WhiteNoiseMiddleware',
)

# use whitenoise in prd
# http://whitenoise.evans.io/en/latest/django.html
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'picha.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'picha.wsgi.application'

from . import database

DATABASES = {
    'default': database.config()
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG:
    USE_DEBUG_TOOLBAR = True
    MIDDLEWARE_CLASSES += \
        ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    ## Can not get Internal_IPS to work for 10.2.2.2 and 172.30.118.161
    INTERNAL_IPS = (
        '10.2.2.2',
        '127.0.0.1',
        '172.30.118.161',
    )

#REDIS_PORT = 6379
#REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
#
#BROKER_URL = 'redis://{host}:{port}'.format(host=REDIS_HOST,port=REDIS_PORT)
#CELERY_RESULT_BACKEND = 'redis://{host}:{port}'.format(host=REDIS_HOST,port=REDIS_PORT)
#
#CELERY_ACCEPT_CONTENT = ['application/json']
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TIMEZONE = 'Africa/Nairobi'
#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'Picha <picha@example.com>'
