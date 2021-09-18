# -*- coding: utf-8 -*-
from django.templatetags import l10n
from rest_framework import serializers

from backend.api.uauth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['uid', 'name', 'email', 'last_login']
