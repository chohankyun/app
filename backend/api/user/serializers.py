# -*- coding: utf-8 -*-
from rest_framework import serializers

from backend.api.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
