# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import UserRequest, UserProfile

# Register your models HERE
class UserRequestAdmin(admin.ModelAdmin):
	class Meta:
		model = UserRequest

admin.site.register(UserRequest, UserRequestAdmin)

class UserProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
