# -*- coding: utf-8 -*-
from calendar import timegm
from datetime import datetime

import jwt

from backend.drf.settings import JWT_AUTH


class Handler:
    def __init__(self, salt='salt'):
        self.salt = str(salt)

    def get_jwt_key(self):
        return JWT_AUTH['JWT_SECRET_KEY'] + self.salt

    @staticmethod
    def get_jwt_payload(data_for_payload):
        payload = data_for_payload.copy()
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

