# -*- coding: utf-8 -*-
import hashlib


class HttpSalt:
    def __init__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0] if request.META.get('HTTP_X_FORWARDED_FOR') else None
        client_ip = x_forwarded_for or request.META.get('REMOTE_ADDR', 'client_ip')
        host = request.META.get('HTTP_HOST', 'host')
        user_agent = request.META.get('HTTP_USER_AGENT', 'user_agent')
        connection = request.META.get('HTTP_CONNECTION', 'connection')
        accept = request.META.get('HTTP_ACCEPT', 'accept')
        accept_encoding = request.META.get('HTTP_ACCEPT_ENCODING', 'accept_encoding')
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'accept_language')
        referer = request.META.get('HTTP_REFERER', 'referer')
        salt_data_list = [client_ip, host, user_agent, connection, accept, accept_encoding, accept_language, referer]
        self.salt = hashlib.md5(','.join(salt_data_list).encode()).hexdigest()

    def __str__(self):
        return self.salt
