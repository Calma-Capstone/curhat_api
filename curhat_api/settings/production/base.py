from curhat_api.settings.components.base import REST_FRAMEWORK
import environ
import os
import io
from urllib.parse import urlparse

env = environ.Env()
env.read_env(io.StringIO(os.environ.get("AUTH_SECRET", None)))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG", default=True)

ALLOWED_HOSTS = ["*"]

CALMA_FRONTEND_URL = env("CALMA_FRONTEND_URL", default=None)
if CALMA_FRONTEND_URL:
    CORS_ALLOWED_ORIGINS = [CALMA_FRONTEND_URL]
else:
    CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
