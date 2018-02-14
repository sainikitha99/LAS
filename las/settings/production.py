from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'las_prod', # database_name
        'USER': 'las_prod', # database_user
        'PASSWORD': 'las1pass', # password
        'HOST': 'www.las.com', # host
        'PORT': '5432' # default port for postgres.
    }
}