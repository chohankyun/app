# -*- coding: utf-8 -*-
class JSONWebTokenUser:
    def __init__(self, user: (object, dict)):
        self.id = getattr(user, 'id', None) or user.get('id')
        self.name = getattr(user, 'name', None) or user.get('name')
        self.group = str(user.groups.first()) if hasattr(user, 'groups') else None or user.get('group')
        self.is_authenticated = True if self.id else False
