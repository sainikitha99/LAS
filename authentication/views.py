# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def user_registration(request):
	return render(request, 'user_reg.html')

def hospital_registration(request):
	return render(request, 'hospital_reg.html')
