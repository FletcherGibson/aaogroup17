from aao_cutout_api.settings.base import *
import os
#Override base.py settings here

ALLOWED_HOSTS = ['aao-api-test.ap-southeast-2.elasticbeanstalk.com',
                 '13.236.38.167',]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATIC_ROOT = os.path.join(ROOT_DIR, "..", "www", "static")
STATIC_URL = '/static/'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

try:
    from aao_cutout_api.settings.local import *
except :
    pass