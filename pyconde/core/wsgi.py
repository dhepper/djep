"""
WSGI config for reelport project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os
from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconde.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

application = get_wsgi_application()