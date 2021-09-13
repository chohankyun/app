# -*- coding: utf-8 -*-
from django.templatetags import l10n
from rest_framework import serializers

from backend.api.user.models import User


class UserSerializer(serializers.ModelSerializer):
    local_last_login = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['app_id', 'name', 'email', 'local_last_login']

    @staticmethod
    def get_local_last_login(obj):
        return l10n.localize(obj.last_login)
