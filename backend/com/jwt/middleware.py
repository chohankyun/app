# -*- coding: utf-8 -*-
from rest_framework import status

from backend.com.jwt.handler import HttpHandler


class JSONWebTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if getattr(request.user, 'is_authenticated', None):
            http_handler = HttpHandler()
            jwt = http_handler.get_jwt(request)
            response.set_cookie('token', value=jwt)

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.delete_cookie('token')

        return response
