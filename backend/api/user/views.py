# -*- coding: utf-8 -*-
import random
import string

from django.contrib.auth import authenticate
from django.contrib.auth import user_logged_in
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.http import HttpResponse
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode as uid_decoder, urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied, ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from backend.api.user.models import User
from backend.com.email.confirmation import EmailConfirmationHMAC
from backend.com.email.email import EmailMixin
from backend.com.jwt.handler import jwt_user


class IsAuth(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)


class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, *args, **kwargs):
        return Response(data={'detail': _('Logout')}, status=status.HTTP_401_UNAUTHORIZED)


class Login(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.login(app_id=request.data['app_id'], password=request.data['password'])
        request.user = jwt_user(user)
        return Response(request.user.__dict__, status=status.HTTP_200_OK)

    def login(self, **credentials):
        user = authenticate(**credentials)

        if not user:
            raise AuthenticationFailed(detail=_('The id or password do not match.'))
        if not user.is_active:
            raise AuthenticationFailed(detail=_('This is disabled id.'))
        if not user.is_email_verified:
            raise PermissionDenied(detail=_('Email verification has not been completed.'))
        if user.is_staff or user.is_superuser:
            raise PermissionDenied(detail=_('You do not have permission.'))

        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        return user


class Register(GenericAPIView, EmailMixin):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.register()
        self.send_email(user, 'auth/email_confirm_subject.txt', 'auth/email_confirm_email.html')
        return Response('Verification email sent.', status=status.HTTP_200_OK)

    def register(self):
        if self.request.data['password'] != self.request.data['re_password']:
            raise ParseError(detail="The two password fields didn't match.")
        if User.objects.filter(app_id=self.request.data['app_id']).exists():
            raise ParseError(detail='A user is already registered with this username.')
        if User.objects.filter(email=self.request.data['email']).exists():
            raise ParseError(detail='A user is already registered with this email.')

        user_item_names = [field.name for field in User._meta.fields if field.name != 'id']
        register_data = {key: self.request.data[key] for key in self.request.data if key in user_item_names}
        user = User.objects.create_user(**register_data)
        return user

    def get_extras(self, user):
        confirmation = EmailConfirmationHMAC(user.email)
        return {'activate_url': confirmation.get_email_confirmation_url(self.request, confirmation)}


class EmailConfirm(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, **kwargs):
        confirmation = EmailConfirmationHMAC.from_key(self.kwargs['key'])
        if not confirmation:
            raise ParseError(detail='Invalid key.')
        if not confirmation.confirm():
            raise ParseError(detail='E-mail address matching query does not exist.')
        return HttpResponse(_('Your email has been verified.'))


class AppIdFind(GenericAPIView, EmailMixin):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = User.objects.filter(email=self.request.data['email']).first()
        if not user:
            raise AuthenticationFailed(detail='E-mail address matching query does not exist.')
        if not user.is_active:
            raise PermissionDenied(detail='User account is disabled.')

        self.send_email(user, 'auth/app_id_find_subject.txt', 'auth/app_id_find_email.html')
        return Response('Your username has been sent to your e-mail address.')


class PasswordReset(GenericAPIView, EmailMixin):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = User.objects.filter(email=self.request.data['email']).first()
        if not user:
            raise AuthenticationFailed(detail='E-mail address matching query does not exist.')
        if not user.is_active:
            raise PermissionDenied(detail='User account is disabled.')

        self.send_email(user, 'auth/password_reset_subject.txt', 'auth/password_reset_email.html')
        return Response('Password reset e-mail has been sent.')

    def get_extras(self, user):
        return {
            'password': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': PasswordResetTokenGenerator().make_token(user),
            'host': self.request.get_host()
        }


class PasswordResetConfirm(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(uid_decoder(self.kwargs['uid']))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise AuthenticationFailed(detail='user matching query does not exist.')
        if not default_token_generator.check_token(user, self.kwargs['token']):
            raise AuthenticationFailed(detail='Invalid token.')

        self.reset_password(user)
        return HttpResponse(_('Password has been reset with the new password.'))

    def reset_password(self, user):
        password = self.kwargs['password']
        user.set_password(password)
        user.save()


class PasswordChange(GenericAPIView, EmailMixin):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=self.request.user.id)
        except User.DoesNotExist:
            raise AuthenticationFailed(detail='User matching query does not exist.')

        if not user.is_active:
            raise AuthenticationFailed(detail='User account is disabled.')

        if not user.check_password(self.request.data['old_password']):
            raise AuthenticationFailed(detail='Invalid old password.')

        if self.request.data['new_password1'] != self.request.data['new_password2']:
            raise AuthenticationFailed(detail="The two password fields didn't match.")

        self.change_password(user)
        self.send_email(user, 'auth/password_changed_subject.txt', 'auth/password_changed_email.html')
        return Response('Password has been changed with the new password.')

    def get_extras(self, user):
        return {
            'old_password': self.request.data['old_password'],
            'new_password': self.request.data['new_password1']
        }

    def change_password(self, user):
        password = self.request.data["new_password1"]
        user.set_password(password)
        user.save()
