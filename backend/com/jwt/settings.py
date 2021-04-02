import datetime
from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

DEFAULTS = {
    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60 * 30),
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=5),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': 'token',
    'JWT_USER': 'backend.com.jwt.handler.User',
    'JWT_SALT': 'backend.com.jwt.handler.Salt',
}

IMPORT_STRINGS = (
    'JWT_USER',
    'JWT_SALT',
)

jwt_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)

