# -*- coding: utf-8 -*-
from calendar import timegm
from datetime import datetime

import hashlib
import jwt

from backend.drf.settings import JWT_AUTH


class BaseHandler:
    salt = 'salt'

    def get_jwt_key(self):
        return JWT_AUTH['JWT_SECRET_KEY'] + self.salt

    @staticmethod
    def get_base_payload(data_for_payload):
        return {
            'id': data_for_payload.get('id'),
            'name': data_for_payload.get('name'),
            'group_name': data_for_payload.get('group_name')
        }

    def get_jwt_payload(self, data_for_payload):
        payload = self.get_base_payload(data_for_payload)
        payload['exp'] = datetime.utcnow() + JWT_AUTH['JWT_EXPIRATION_DELTA']

        if JWT_AUTH['JWT_ALLOW_REFRESH']:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        if JWT_AUTH['JWT_AUDIENCE']:
            payload['aud'] = JWT_AUTH['JWT_AUDIENCE']

        if JWT_AUTH['JWT_ISSUER']:
            payload['iss'] = JWT_AUTH['JWT_ISSUER']

        return payload

    def jwt_encode_payload(self, payload):
        key = self.get_jwt_key()
        return jwt.encode(payload, key, JWT_AUTH['JWT_ALGORITHM'])

    def jwt_decode_token(self, token):
        key = self.get_jwt_key()
        options = {
            'verify_exp': JWT_AUTH['JWT_VERIFY_EXPIRATION'],
        }
        return jwt.decode(
            token,
            key,
            options=options,
            leeway=JWT_AUTH['JWT_LEEWAY'],
            audience=JWT_AUTH['JWT_AUDIENCE'],
            issuer=JWT_AUTH['JWT_ISSUER'],
            algorithms=[JWT_AUTH['JWT_ALGORITHM']])


class HttpHandler(BaseHandler):
    def __init__(self, request):
        self.request = request
        self.salt = self.get_http_salt()

    def get_http_salt(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0] if self.request.META.get('HTTP_X_FORWARDED_FOR') else None
        client_ip = x_forwarded_for or self.request.META.get('REMOTE_ADDR', 'client_ip')
        host = self.request.META.get('HTTP_HOST', 'host')
        user_agent = self.request.META.get('HTTP_USER_AGENT', 'user_agent')
        connection = self.request.META.get('HTTP_CONNECTION', 'connection')
        accept = self.request.META.get('HTTP_ACCEPT', 'accept')
        accept_encoding = self.request.META.get('HTTP_ACCEPT_ENCODING', 'accept_encoding')
        accept_language = self.request.META.get('HTTP_ACCEPT_LANGUAGE', 'accept_language')
        referer = self.request.META.get('HTTP_REFERER', 'referer')
        salt_data_list = [client_ip, host, user_agent, connection, accept, accept_encoding, accept_language, referer]
        return hashlib.md5(','.join(salt_data_list).encode()).hexdigest()

    def get_jwt_user(self, payload):
        jwt_user_data = self.get_base_payload(payload)
        jwt_user_data['is_authenticated'] = True
        return type('jwt_user', (object,), jwt_user_data), jwt_user_data

    def get_jwt(self):
        user = self.request.user
        payload = self.get_jwt_payload(user.__dict__)
        return self.jwt_encode_payload(payload)

    def get_payload(self, jwt_value):
        return self.jwt_decode_token(jwt_value)
