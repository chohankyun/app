# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from backend.drf import settings


class BaseEmailMixin:
    def get_extras(self, user):
        """Override this method to add extra options"""
        return {}

    def make_email(self, user, subject_template_name, email_template_name):
        current_site = get_current_site(self.request)
        site_name = current_site.name
        domain = current_site.domain

        opt = {
            'domain': domain,
            'site_name': site_name,
            'app_id': user.app_id,
            'name': user.name,
            'email': user.email,
            'protocol': 'https' if self.request.is_secure() else 'http',
        }

        opt.update(self.get_extras(user))
        subject = loader.render_to_string(subject_template_name, opt)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, opt)
        return EmailMultiAlternatives(subject, body, settings.DEFAULT_FROM_EMAIL, [user.email])


class EmailMixin(BaseEmailMixin):
    def send_email(self, user, subject_template_name, email_template_name):
        email_message = self.make_email(user, subject_template_name, email_template_name)
        email_message.send()


class EmailAttachMixin(BaseEmailMixin):
    def send_email(self, user, subject_template_name, email_template_name, attach_file):
        email_message = self.make_email(user, subject_template_name, email_template_name)
        email_message.attach(**attach_file)
        return email_message.send()
