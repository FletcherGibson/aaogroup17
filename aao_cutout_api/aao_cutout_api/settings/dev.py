from aao_cutout_api.settings.base import *

#Override base.py settings here
SECRET_KEY = env('DJANGO_SECRET_KEY', default='apqga4h8g=n6x!oh-6976x4q%^+iadbqwj%p+$an0(j)8c2b^f') #os.environ['SECRET_KEY']

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