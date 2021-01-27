# -*- coding: utf-8 -*-
from backend.common.jwt.handler import HttpHandler


class JSONWebTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if getattr(request.user, 'is_authenticated', None):
            http_handler = HttpHandler()
            jwt = http_handler.get_jwt(request)
            response.set_cookie('token', value=jwt)
        else:
            response.delete_cookie('token')
        return response
