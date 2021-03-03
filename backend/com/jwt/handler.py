# -*- coding: utf-8 -*-
import hashlib
from calendar import timegm
from datetime import datetime

import jwt

from backend.com.jwt.settings import jwt_settings


class Salt:
    def __init__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0] if request.META.get('HTTP_X_FORWARDED_FOR') else None
        client_ip = x_forwarded_for or request.META.get('REMOTE_ADDR', 'client_ip')
        host = request.META.get('HTTP_HOST', 'host')
        user_agent = request.META.get('HTTP_USER_AGENT', 'user_agent')
        connection = request.META.get('HTTP_CONNECTION', 'connection')
        accept_encoding = request.META.get('HTTP_ACCEPT_ENCODING', 'accept_encoding')
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'accept_language')
        salt_data_list = [client_ip, host, user_agent, connection, accept_encoding, accept_language]
        self.salt = hashlib.md5(','.join(salt_data_list).encode()).hexdigest()

    def __str__(self):
        return self.salt


class User:
    def __init__(self, user: (object, dict)):
        self.id = getattr(user, 'id', None) or user.get('id')
        self.name = getattr(user, 'name', None) or user.get('name')
        self.group = str(user.groups.first()) if hasattr(user, 'groups') else None or user.get('group')
        self.is_authenticated = True if self.id else False


class Token:
    def __init__(self, salt='salt'):
        self.salt = str(salt)

    def get_jwt_key(self):
        return jwt_settings.JWT_SECRET_KEY + self.salt

    @staticmethod
    def get_jwt_payload(data_for_payload):
        payload = data_for_payload.copy()
        payload['exp'] = datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA

        if jwt_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        if jwt_settings.JWT_AUDIENCE:
            payload['aud'] = jwt_settings.JWT_AUDIENCE

        if jwt_settings.JWT_ISSUER:
            payload['iss'] = jwt_settings.JWT_ISSUER

        return payload

    def jwt_encode_payload(self, payload):
        key = self.get_jwt_key()
        return jwt.encode(payload, key, jwt_settings.JWT_ALGORITHM)

    def jwt_decode_token(self, token):
        key = self.get_jwt_key()
        options = {
            'verify_exp': jwt_settings.JWT_VERIFY_EXPIRATION,
        }
        return jwt.decode(
            token,
            key,
            options=options,
            leeway=jwt_settings.JWT_LEEWAY,
            audience=jwt_settings.JWT_AUDIENCE,
            issuer=jwt_settings.JWT_ISSUER,
            algorithms=[jwt_settings.JWT_ALGORITHM])


jwt_user = jwt_settings.JWT_USER
jwt_salt = jwt_settings.JWT_SALT
