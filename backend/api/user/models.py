# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from encrypted_fields import fields


class AppUserManager(UserManager):
    def _create_user(self, app_id, email, password, **extra_fields):
        if not app_id:
            raise ValueError('The given app_id must be set')
        email = self.normalize_email(email)
        app_id = self.model.normalize_username(app_id)
        user = self.model(app_id=app_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, app_id, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(app_id, email, password, **extra_fields)

    def create_superuser(self, app_id, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(app_id, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    app_id_validator = UnicodeUsernameValidator()

    app_id = models.CharField(_('application identifier'), max_length=150, unique=True, validators=[app_id_validator])
    name = models.CharField(_('user name'), max_length=150, blank=False)
    encrypt_email = fields.EncryptedEmailField(_('email address'), blank=False)
    email = fields.SearchField(hash_key="secret_hash", encrypted_field_name="encrypt_email", unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_email_verified = models.BooleanField(_('email verified'), default=False)
    created_datetime = models.DateTimeField(_('created datetime'), auto_now_add=True)
    updated_datetime = models.DateTimeField(_('updated datetime'), auto_now=True)

    objects = AppUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'app_id'
    REQUIRED_FIELDS = ['name', 'email']

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.app_id
