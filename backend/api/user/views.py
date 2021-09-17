# -*- coding: utf-8 -*-
import random
import string

from django.contrib.auth import authenticate
from django.contrib.auth import user_logged_in
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.http import HttpResponse
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode as uid_decoder, urlsafe_base64_encode
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied, ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.api.user.models import User
from backend.api.user.serializers import UserSerializer
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
        return Response(data={'detail': 'Logout'}, status=status.HTTP_401_UNAUTHORIZED)


class Login(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.login(uid=request.data['uid'], password=request.data['password'])
        request.user = jwt_user(user)
        return Response(request.user.__dict__, status=status.HTTP_200_OK)

    def login(self, **credentials):
        user = authenticate(**credentials)

        if not user:
            raise AuthenticationFailed(detail='The uid or password do not match.')
        if not user.is_active:
            raise AuthenticationFailed(detail='This is disabled uid.')
        if not user.is_email_verified:
            raise PermissionDenied(detail='The email verification has not been completed.')
        if user.is_staff or user.is_superuser:
            raise PermissionDenied(detail='You do not have permission.')

        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        return user


class Register(GenericAPIView, EmailMixin):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.register()
        self.send_email(user, 'auth/email_confirm_subject.txt', 'auth/email_confirm_email.html')
        return Response({'detail': 'Verification email sent.'}, status=status.HTTP_200_OK)

    def register(self):
        if self.request.data['password'] != self.request.data['re_password']:
            raise ParseError(detail="The two password fields didn't match.")
        if User.objects.filter(uid=self.request.data['uid']).exists():
            raise ParseError(detail='This uid is already registered.')
        if User.objects.filter(email=self.request.data['email']).exists():
            raise ParseError(detail='This email is already registered.')

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
            raise ParseError(detail='Invalid verification information.')
        if not confirmation.confirm():
            raise ParseError(detail='This email does not exist.')

        accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        lang = accept_language.split(',')[0][:2]

        with translation.override(lang):
            message = _('Your email has been verified.')
        return HttpResponse(message)


class UidFind(GenericAPIView, EmailMixin):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = User.objects.filter(email=self.request.data['email']).first()
        if not user:
            raise AuthenticationFailed(detail='This email does not exist.')
        if not user.is_active:
            raise PermissionDenied(detail='This is disabled uid.')

        self.send_email(user, 'auth/uid_find_subject.txt', 'auth/uid_find_email.html')
        return Response({'detail': 'Your uid has been sent to your email.'})


class PasswordReset(GenericAPIView, EmailMixin):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = User.objects.filter(email=self.request.data['email']).first()
        if not user:
            raise AuthenticationFailed(detail='This email does not exist.')
        if not user.is_active:
            raise PermissionDenied(detail='This is disabled uid.')

        self.send_email(user, 'auth/password_reset_subject.txt', 'auth/password_reset_email.html')
        return Response({'detail': 'Password reset email has been sent.'})

    def get_extras(self, user):
        return {
            'password': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
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
            raise AuthenticationFailed(detail='The uid does not exist.')

        if not default_token_generator.check_token(user, self.kwargs['token']):
            raise AuthenticationFailed(detail='Invalid token information.')

        self.reset_password(user)

        accept_language = self.request.META['HTTP_ACCEPT_LANGUAGE']
        lang = accept_language.split(',')[0][:2]

        with translation.override(lang):
            message = _('Password has been reset with the new password.')
        return HttpResponse(message)

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
            raise AuthenticationFailed(detail='The uid does not exist.')

        if not user.is_active:
            raise AuthenticationFailed(detail='This uis disabled id.')

        if not user.check_password(self.request.data['old_password']):
            raise AuthenticationFailed(detail='Invalid old password.')

        if self.request.data['new_password'] != self.request.data['new_re_password']:
            raise AuthenticationFailed(detail="The two password fields didn't match.")

        self.change_password(user)
        self.send_email(user, 'auth/password_changed_subject.txt', 'auth/password_changed_email.html')
        return Response({'detail': 'Password has been changed with the new password.'})

    def get_extras(self, user):
        return {
            'old_password': self.request.data['old_password'],
            'new_password': self.request.data['new_password']
        }

    def change_password(self, user):
        password = self.request.data["new_password"]
        user.set_password(password)
        user.save()


class UserSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        if str(request.user.id) != self.kwargs.get('pk'):
            raise ParseError(detail='Invalid user identifier information.')
        return super(UserSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if str(request.user.id) != self.kwargs.get('pk'):
            raise ParseError(detail='Invalid user identifier information.')
        return super(UserSet, self).update(request, *args, **kwargs)
