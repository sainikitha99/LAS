# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.gis.geos import Point

from core.models import UserProfile


def user_registration(request):
	if request.POST is not None and request.POST != {}:

		data = request.POST
		# Validate password and return error
		if not request.user.is_authenticated:
			if data['password'] != data['confirm_password']:
				messages.error(request, "Passwords didn't match")
				return render(request, 'user_reg.html')

		user_obj = None
		if request.user.is_authenticated:
			user_obj = User.objects.get(id=request.user.id)
		else:
			user_obj = User()
		user_obj.email = data['email']
		user_obj.first_name = data['first_name']
		user_obj.last_name = data['last_name']
		username = user_obj.first_name
		if user_obj.last_name:
			username = username + user_obj.last_name
		user_obj.username = username.lower()
		if not request.user.is_authenticated:
			user_obj.set_password(data['password'])
		user_obj.save()

		user_profile = None
		if request.user.is_authenticated:
			# get_or_create is used while creating profile when user logged in via Google.
			user_profile, created = UserProfile.objects.get_or_create(user=request.user)
		else:
			user_profile = UserProfile()
			user_profile.user = user_obj
		user_profile.gender = data['gender']
		user_profile.dob = data['dob']
		user_profile.mobile_number = int(data['mobile'])
		if "alternate_mobile" in data and data['alternate_mobile'] != "" and data['alternate_mobile'] is not None:
			user_profile.alternate_number = int(data['alternate_mobile'])
		user_profile.blood_group = data['blood_group']

		user_profile.address = data["formatted_address"]
		user_profile.save()

		if request.user.is_authenticated:
			messages.success(request, "User Updated.")
			return redirect('view_profile')
		messages.success(request, "User successfully created.")

	return render(request, 'user_reg.html')


def login_view(request):
	if request.POST is not None and request.POST != {}:

		isHospital = False
		hos_reg_id = ""
		user_q = []
		if "hos_reg_id" in request.POST:
			hos_reg_id = request.POST['hos_reg_id']
			hospitalprofile = UserProfile.objects.filter(hos_reg_id=hos_reg_id).first()
			user_q = User.objects.filter(id=hospitalprofile.user.id)
		else:
			email = request.POST['email']
			user_q = User.objects.filter(email=email)

		password = request.POST['password']
		if user_q.exists():
			user_obj = user_q.first()
			username = user_obj.username

			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				messages.success(request, "Logged In successfully")
				return redirect('/')
		else:
			if isHospital:
				messages.error(request, "Hospital does not exists.")
			else:
				messages.error(request, "User does not exists.")
			return render(request, 'base.html')

	return render(request, 'base.html')


def logout_view(request):
	logout(request)
	return redirect('/')


def hospital_registration(request):
	if request.POST is not None and request.POST !={}:
		data=request.POST
		if data['password'] != data['confirm_password']:
			messages.error(request, "passwords didn't match")
			return render(request, 'hospital_reg.html')

		usr_obj = User()

		usr_obj.email = data['hospital_email']

		usr_obj.username = data['hospital_name'].lower().replace(" ","")
		usr_obj.set_password(data['password'])
		usr_obj.save()

		hos_profile = UserProfile()
		hos_profile.user = usr_obj
		hos_profile.hos_reg_id = data['hos_reg_id']
		hos_profile.hos_reg_date = data['hos_reg_date']
		hos_profile.hos_dir_name = data['hos_dir_name']
		hos_profile.ambulance_count = data['ambulance_count']
		hos_profile.is_hospital = True
		hos_profile.latitude = data["latitude"]
		hos_profile.longitude = data["longitude"]
		hos_profile.location_point = Point(float(data["longitude"]), float(data["latitude"]))

		hos_profile.address = data["formatted_address"]
		hos_profile.save()
		messages.success(request, "Hospital Registration successfully completed")
 	return render(request, 'hospital_reg.html')


def view_profile(request):
	if request.user.is_authenticated.value == True:
		try:
			context = {}
			user_obj = User.objects.get(id=request.user.id)
			try:
				userprofile = user_obj.userprofile
			except:
				context['google_auth'] = True
				return render(request, 'edit_profile.html', context)
			context["gender"] = user_obj.userprofile.gender
			context["dateOfBirth"] = user_obj.userprofile.dob
			context["bloodGroup"] = user_obj.userprofile.blood_group
			context["mobileNumber"] = user_obj.userprofile.mobile_number
			context["alternateNumber"] = user_obj.userprofile.alternate_number
			context["address"] = user_obj.userprofile.address
			return render(request, 'view_profile.html', context)
		except:
			return render(request, 'edit_profile.html')
	else:
		return redirect('/')


def edit_profile(request):
	if request.user.is_authenticated.value == True:
		context = {}
		user_obj = User.objects.get(id=request.user.id)
		try:
			userprofile = user_obj.userprofile
		except:
			context['google_auth'] = True
			return render(request, 'edit_profile.html', context)
		context["gender"] = user_obj.userprofile.gender
		day = str(user_obj.userprofile.dob.day)
		month = str(user_obj.userprofile.dob.month)
		year = str(user_obj.userprofile.dob.year)
		if len(str(user_obj.userprofile.dob.day)) == 1:
			day = "0"+ day
		if len(str(user_obj.userprofile.dob.month)) == 1:
			month = "0"+ month
		if len(str(user_obj.userprofile.dob.year)) == 1:
			year = "0"+ year
		context["dateOfBirth"] = "{}-{}-{}".format(year, month, day)
		context["bloodGroup"] = user_obj.userprofile.blood_group
		context["mobileNumber"] = user_obj.userprofile.mobile_number
		context["alternateNumber"] = user_obj.userprofile.alternate_number
		context["address"] = user_obj.user_profile.address
		return render(request, 'edit_profile.html', context)
	else:
		return redirect('/')


def reset_password(request):
	if request.POST is not None and request.POST !={}:
		data = request.POST
		if "hosp_id" in data:
			userprofile = UserProfile.objects.get(hos_reg_id=data["hosp_id"])
			user = userprofile.user
			user.set_password(data["new_password"])
			user.save()
		else:
			user = User.objects.get(email=data["user_email"])
			user.set_password(data["new_password"])
			user.save()
			messages.success(request, "Password Reset successfully")
	if "is_user" in request.GET:
		return render(request, 'reset_password.html', {"is_user": True})
	elif "is_hospital" in request.GET:
		return render(request, 'reset_password.html', {"is_hospital": True})
	return render(request, 'reset_password.html')
