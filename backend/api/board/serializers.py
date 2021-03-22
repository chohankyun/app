# -*- coding: utf-8 -*-
from rest_framework import serializers

from backend.api.board.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
