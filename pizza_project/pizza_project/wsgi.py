"""
WSGI config for pizza_project_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza_project_api.settings')
from dotenv import load_dotenv
load_dotenv()
env = os.getenv('ENV','development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'pizza_project.settings.{env}')

application = get_wsgi_application()
