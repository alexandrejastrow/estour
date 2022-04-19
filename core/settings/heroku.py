from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
import environ
from core.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', default=False)

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


sentry_sdk.init(
    dsn="https://9d132ac8a1834e2d804e06e4409314e2@o1198631.ingest.sentry.io/6321155",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
ROOT_URLCONF = 'core.urls'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# email
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = env('EMAIL_HOST')
