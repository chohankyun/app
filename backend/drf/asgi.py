"""
ASGI config for drf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import sys
import django

# from django.core.asgi import get_asgi_application
from channels.routing import get_default_application

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

django.setup()

application = get_default_application()
