from .base  import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_NAME', 'postgres'),
        'USER': environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': environ.get('POSTGRES_PORT', '5432'),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
    }
}