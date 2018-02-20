# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import HospitalProfile

# Register your models HERE
class HospitalProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'hos_reg_id', 'ambulance_count')



admin.site.register(HospitalProfile, HospitalProfileAdmin)
