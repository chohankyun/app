# -*- coding: utf-8 -*-
from calendar import timegm
from datetime import datetime

import jwt

from backend.drf.settings import JWT_AUTH


class BaseHandler:
    @staticmethod
    def get_jwt_secret_key():
        """
            나중에 키 관련 로직 추가
        """
        if JWT_AUTH['JWT_GET_USER_SECRET_KEY']:
            key = str(JWT_AUTH['JWT_GET_USER_SECRET_KEY'])
            return key
        return JWT_AUTH['JWT_SECRET_KEY']

    @staticmethod
    def get_base_payload(data_for_payload):
        return {
            'id': data_for_payload.get('id'),
            'name': data_for_payload.get('name'),
            'group_name': data_for_payload.get('group_name')
        }

    def get_jwt_payload(self, data_for_payload):
        payload = self.get_base_payload(data_for_payload)
        payload['client_ip'] = data_for_payload.get('client_ip')
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
        key = JWT_AUTH['JWT_PRIVATE_KEY'] or self.get_jwt_secret_key()
        return jwt.encode(payload, key, JWT_AUTH['JWT_ALGORITHM'])

    def jwt_decode_token(self, token):
        options = {
            'verify_exp': JWT_AUTH['JWT_VERIFY_EXPIRATION'],
        }
        secret_key = self.get_jwt_secret_key()
        return jwt.decode(
            token,
            JWT_AUTH['JWT_PUBLIC_KEY'] or secret_key,
            options=options,
            leeway=JWT_AUTH['JWT_LEEWAY'],
            audience=JWT_AUTH['JWT_AUDIENCE'],
            issuer=JWT_AUTH['JWT_ISSUER'],
            algorithms=[JWT_AUTH['JWT_ALGORITHM']])


class HttpHandler(BaseHandler):
    def get_jwt_user(self, data_for_payload):
        jwt_user_data = self.get_base_payload(data_for_payload)
        jwt_user_data['is_authenticated'] = True
        return type('jwt_user', (object,), jwt_user_data), jwt_user_data

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]
        else:
            client_ip = request.META.get('REMOTE_ADDR')
        return client_ip

    def get_jwt(self, request):
        data_for_payload = dict(request.user.__dict__)
        data_for_payload['client_ip'] = self.get_client_ip(request)
        payload = self.get_jwt_payload(data_for_payload)
        return self.jwt_encode_payload(payload)
