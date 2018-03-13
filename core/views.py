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
def dashboard(request):
	return render(request, 'dashboard.html')
def requesth(request):
	return render(request, 'request.html')
def notifications(request):
	return render(request, 'notifications.html')
def feedback(request):
	return render(request, 'feedback.html')
def userdashboard(request):
	return render(request, 'userdashboard.html')
def user_request(request):
	return render(request, 'user_request.html')
def my_requests(request):
	return render(request, 'my_requests.html')
def give_feedback(request):
	return render(request, 'give_feedback.html')
