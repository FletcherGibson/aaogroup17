from aao_cutout_api.settings.base import *

#Override base.py settings here

DEBUG = env.bool('DJANGO_DEBUG', default=True)

# Local sqlite3 DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}

try:
    from aao_cutout_api.settings.local import *
except :
    pass