# -*- coding: utf-8 -*-
from django.contrib import admin

from backend.api.board.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'updated_datetime']
    list_display = [field.name for field in Category._meta.fields]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_datetime', 'updated_datetime']
    list_display = [field.name for field in Post._meta.fields]
