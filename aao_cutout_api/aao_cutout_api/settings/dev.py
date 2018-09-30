from aao_cutout_api.settings.base import *

#Override base.py settings here

DEBUG = True

# Local sqlite3 DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from aao_cutout_api.settings.local import *
except :
    pass