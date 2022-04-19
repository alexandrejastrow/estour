from sentry_sdk.integrations.django import DjangoIntegration
import environ
from core.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env('API_KEY'),
    'API_SECRET': env('API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DATABASES = {
    'default': env.db(),
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# email
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = env('EMAIL_HOST')
