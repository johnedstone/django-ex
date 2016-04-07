import os
from kombu import Exchange, Queue
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
    'experiences',
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
)

ROOT_URLCONF = 'picha.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

redis_service_name = os.getenv('REDIS_SERVICE_NAME','').upper()
REDIS_HOST = os.environ.get('{}_SERVICE_HOST'.format(redis_service_name))
REDIS_PORT = os.getenv('{}_SERVICE_PORT'.format(redis_service_name))
fh = open('/tmp/myenv', 'w')
fh.write('REDIS_HOST:{}\n'.format(REDIS_HOST))
fh.write('REDIS_PORT:{}\n'.format(REDIS_PORT))

REDIS_PORT_A = 6379
REDIS_HOST_A = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
REDIS_PORT = 6379
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
fh.write('REDIS_HOST_A:{}\n'.format(REDIS_HOST_A))
fh.write('REDIS_PORT_A:{}\n'.format(REDIS_PORT_A))
fh.close()

# https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/ Step 3
BROKER_URL = 'redis://{host}:{port}'.format(host=REDIS_HOST,port=REDIS_PORT)
CELERY_RESULT_BACKEND = 'redis://{host}:{port}'.format(host=REDIS_HOST,port=REDIS_PORT)

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

## For later
# REDIS_DB = 0
fh.write('REDIS_HOST_A:{}\n'.format(REDIS_HOST_A))
fh.write('REDIS_PORT_A:{}\n'.format(REDIS_PORT_A))
fh.close()

# https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/ Step 3
BROKER_URL = 'redis://{host}:{port}'.format(host=REDIS_HOST,port=REDIS_PORT)
CELERY_RESULT_BACKEND = 'redis://{host}:{port}'.format(host=REDIS_HOST,port=REDIS_PORT)

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

## For later
# REDIS_DB = 0
# CELERY_ALWAYS_EAGER = False
# CELERY_ACKS_LATE = True
# CELERY_TASK_PUBLISH_RETRY = True
# CELERY_DISABLE_RATE_LIMITS = False
# CELERY_IGNORE_RESULT = True
# CELERY_SEND_TASK_ERROR_EMAILS = False
# CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
# CELERY_REDIS_MAX_CONNECTIONS = 1
# CELERY_TASK_RESULT_EXPIRES = 600
# CELERY_TASK_SERIALIZER = "json"
# CELERYD_HIJACK_ROOT_LOGGER = False
# CELERYD_PREFETCH_MULTIPLIER = 1
# CELERYD_MAX_TASKS_PER_CHILD = 1000
# CELERY_ACCEPT_CONTENT = ['application/json']

if DEBUG:
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    DEFAULT_FROM_EMAIL = 'Picha <picha@example.com>'
