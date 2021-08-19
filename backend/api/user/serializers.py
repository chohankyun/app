# -*- coding: utf-8 -*-
from rest_framework import serializers

from backend.api.user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # many to many 처리
        exclude = ['groups', 'user_permissions']

    def create_user(self):
        User.objects.create_user(**self.validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



