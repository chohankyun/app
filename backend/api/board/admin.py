# -*- coding: utf-8 -*-
from django.contrib import admin

from backend.api.board.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'updated_datetime']
    list_display = [field.name for field in Category._meta.fields]
