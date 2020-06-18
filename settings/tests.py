# flake8: noqa
from .base import *


# CELERY_BACKEND_URL = 'redis://'

DATABASES = {"default": env.db()}


TEST_RUN = True

BROKER_CONNECTION_TIMEOUT = 1
