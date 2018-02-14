# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from authentication.models import UserRequest


class UserRequestAdmin(admin.ModelAdmin):
	class Meta:
		model = UserRequest

admin.site.register(UserRequest, UserRequestAdmin)
