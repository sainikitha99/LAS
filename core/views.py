# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from core.models import UserRequest, UserProfile


def index(request):
	context = {}
	context["BASE_URI"] = settings.BASE_URI
	if request.user.is_authenticated.value == True:
		try:
			if request.user.userprofile.is_hospital:
				return redirect('hospital_dashboard')
			else:
				user_obj = User.objects.get(id=request.user.id)
				user_profile = user_obj.userprofile
				return redirect('user_dashboard')
		except:
			return redirect('edit_profile')
	return render(request, 'base.html', context)


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
	context = {}
	context["BASE_URI"] = settings.BASE_URI

	if request.user.is_authenticated:
		context["username"] = request.user.first_name
		context["mobile_number"] = request.user.userprofile.mobile_number
	if request.POST is not None and request.POST != {}:

		data = request.POST
		request_obj = UserRequest()
		if request.user.is_authenticated:
			request_obj.user = request.user
			if request.user.userprofile.mobile_number != int(data['mobile']):
				request_obj.mobile = int(data['mobile'])
			else:
				request_obj.mobile = request.user.userprofile.mobile_number
		else:
			request_obj.anonymous_user = data['user_name']
			request_obj.mobile = int(data['mobile'])

		request_obj.count_of_persons_injured = data['injured_count']
		request_obj.severity = data['severity'].lower()
		request_obj.status = data['status'].lower()
		request_obj.latitude = data["latitude"]
		request_obj.longitude = data["longitude"]
		request_obj.save()
		messages.success(request, "User Request Updated.")
	return render(request, 'user_dashboard/raise_request.html', context)


def get_hospitals_near_by(request):
	# GET HOSPITAL WITHIN 5 KM
	hnb = {"items": []}
	if "latitude" in request.GET and "longitude" in request.GET:
		lat = float(request.GET["latitude"])
		lng = float(request.GET["longitude"])
		point = Point(lng, lat)
		hospitals_near_by = UserProfile.objects.filter(location_point__distance_lte=(point, D(km=5)), is_hospital=True)
		for hospital in hospitals_near_by:
			hnb["items"].append({"name": hospital.user.username, "latitude": float(hospital.latitude), "longitude": float(hospital.longitude)})

	return JsonResponse(hnb)


def user_requests(request):
	return render(request, 'user_dashboard/main_requests.html')


def user_feedback(request):
	return render(request, 'user_dashboard/feedback.html')

def requests_list(request):
	return render(request, 'hospital_dashboard/requests_list.html')
