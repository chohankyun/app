# -*- coding: utf-8 -*-
from django.urls import re_path

from backend.api.chat.consumer import Consumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)$', Consumer.as_asgi()),
]
