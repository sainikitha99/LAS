# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from authentication.models import UserRequest



def get_user_requests(request):
	requests = UserRequest.objects.filter(user_id=request.user.id)


def main_page(request):
	requests = UserRequest.objects.all()
	context = {"requests": requests}
	return render(request, 'main_page.html', context)

def user_registration(request):
	requests = UserRequest.objects.all()
	context = {"requests": requests}
	return render(request, 'user_reg.html', context)

def hospital_registration(request):
	requests = UserRequest.objects.all()
	context = {"requests": requests}
	return render(request, 'hospital_reg.html', context)
