# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

from django_oso.oso import Oso

class SnippetsConfig(AppConfig):
    name = 'snippets'
    def ready(self):
        from django.contrib.auth.models import User
        Oso.register_class(User)
