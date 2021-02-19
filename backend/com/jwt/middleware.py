# -*- coding: utf-8 -*-
from rest_framework import status

from backend.com.jwt.handler import Token, jwt_salt


class JSONWebTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return self.jwt_response(request, response)

    @staticmethod
    def jwt_response(request, response):
        if getattr(request.user, 'is_staff', None):
            return response

        if getattr(request.user, 'is_superuser', None):
            return response

        if getattr(request.user, 'is_authenticated', None):
            token = Token(salt=jwt_salt(request))
            payload = token.get_jwt_payload(request.user.__dict__)
            response.set_cookie('token', value=token.jwt_encode_payload(payload), httponly=True, samesite='Lax')

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.delete_cookie('token')

        return response
