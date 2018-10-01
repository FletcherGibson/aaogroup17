from aao_cutout_api.settings.base import *

#Override base.py settings here

DEBUG = True

SECRET_KEY = 'apqga4h8g=n6x!oh-6976x4q%^+iadbqwj%p+$an0(j)8c2b^f'

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