# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index(request):
	if request.user.is_authenticated.value == True:
		user_obj = User.objects.get(id=request.user.id)
		try:
			user_profile = user_obj.userprofile
		except:
			return redirect('edit_profile')
	return render(request, 'base.html')

def overview(request):
	return render(request, 'overview.html')
def contact(request):
	return render(request, 'contact.html')
def about(request):
	return render(request, 'about.html')
