# -*- coding: utf-8 -*-

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from backend.api.chat import routing

application = ProtocolTypeRouter({
    # 'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
