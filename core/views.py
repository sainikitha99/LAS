# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import UserRequest,Address
from django.contrib import messages



def index(request):
	if request.user.is_authenticated.value == True:
		if request.user.userprofile.is_hospital:
			return redirect('hospital_dashboard')
		else:
			user_obj = User.objects.get(id=request.user.id)
			try:
				user_profile = user_obj.userprofile
				return redirect('user_dashboard')
			except:
				return redirect('edit_profile')
	return render(request, 'base.html')


def overview(request):
	return render(request, 'overview.html')


def contact(request):
	return render(request, 'contact.html')


def about(request):
	return render(request, 'about.html')


def hospital_dashboard(request):
	return render(request, 'hospital_dashboard/index.html')


def hospital_requests(request):
	return render(request, 'hospital_dashboard/main_requests.html')


def hospital_notifications(request):
	return render(request, 'hospital_dashboard/notifications.html')


def hospital_feedback(request):
	return render(request, 'hospital_dashboard/feedback.html')


def user_dashboard(request):
	return render(request, 'user_dashboard/index.html')


def raise_request(request):
	if request.POST is not None and request.POST != {}:

		data = request.POST
		print data
		request_obj = UserRequest()
		request_obj.name = data['user_name']
		request_obj.mobile_number = int(data['mobile'])
		address_obj = Address(address1=data['address_1'], city=data['city'], state=data['state'], pincode=data['pincode'], country=data['country'])

		address_obj.save()
		request_obj.address = address_obj
		request_obj.inj_count = data['injured_count']
		request_obj.severity = data['severity']
		request_obj.status = data['status']
		request_obj.save()
		messages.success(request, "User Request Updated.")
	return render(request, 'user_dashboard/raise_request.html')


def user_requests(request):
	return render(request, 'user_dashboard/main_requests.html')


def user_feedback(request):
	return render(request, 'user_dashboard/feedback.html')

def requests_list(request):
	return render(request, 'hospital_dashboard/requests_list.html')
