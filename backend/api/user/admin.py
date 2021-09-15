# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from backend.api.user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('uid', 'password')}),
        (_('Personal info'), {'fields': ('name', 'email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'is_email_verified', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('uid', 'password1', 'password2'),
        }),
    )
    list_display = ('uid', 'name', 'email', 'is_active', 'is_staff', 'last_login', 'is_email_verified', 'created_datetime', 'updated_datetime')
    search_fields = ('uid', 'name', 'email', 'is_staff', 'last_login')
    ordering = ('-updated_datetime',)
    readonly_fields = ('created_datetime', 'updated_datetime')
