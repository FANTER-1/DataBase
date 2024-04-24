"""
WSGI config for Project999 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from app.app import app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project999.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    app.run()