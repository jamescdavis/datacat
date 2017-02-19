import os

from frontend import app as frontend_app
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from werkzeug.wsgi import DispatcherMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datacat.settings")

api_application = get_wsgi_application()
api_application = DjangoWhiteNoise(api_application)

application = DispatcherMiddleware(frontend_app, {
    '/api':     api_application
})
