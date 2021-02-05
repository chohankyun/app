# -*- coding: utf-8 -*-
from rest_framework import status

from backend.com.jwt.handler import Handler
from backend.com.jwt.salt import HttpSalt


class JSONWebTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if getattr(request.user, 'is_authenticated', None):
            handler = Handler(salt=HttpSalt(request))
            payload = handler.get_jwt_payload(request.user.__dict__)
            response.set_cookie('token', value=handler.jwt_encode_payload(payload), httponly=True, samesite='Lax')

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.delete_cookie('token')

        return response
