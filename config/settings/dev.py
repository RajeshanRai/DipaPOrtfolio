from .base import *

DEBUG = True

INSTALLED_APPS += []

# Simple email settings for development: console backend prints messages to console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Dipa Portfolio <no-reply@example.com>'
