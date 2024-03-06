"""
ASGI config for pizza_project_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza_project_api.settings')
from dotenv import load_dotenv
load_dotenv()
env = os.getenv('ENV','development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'pizza_project.settings.{env}')

application = get_asgi_application()