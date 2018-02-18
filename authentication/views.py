# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from core.models import UserProfile, Address


def user_registration(request):
	if request.POST is not None and request.POST != {}:

		data = request.POST
		# Validate password and return error
		if data['password'] != data['confirm_password']:
			messages.error(request, "Passwords didn't match")
			return render(request, 'user_reg.html')

		# create an user and userprofile
		user_obj = User()
		user_obj.email = data['email']
		user_obj.first_name = data['first_name']
		user_obj.last_name = data['last_name']
		username = user_obj.first_name
		if user_obj.last_name:
			username = username + user_obj.last_name
		user_obj.username = username.lower()
		user_obj.set_password(data['password'])
		user_obj.save()

		user_profile = UserProfile()
		user_profile.user = user_obj
		user_profile.gender = data['gender']
		user_profile.dob = data['dob']
		user_profile.mobile_number = int(data['mobile'])
		if "alternate_mobile" in data and data['alternate_mobile'] != "" and data['alternate_mobile'] is not None:
			user_profile.alternate_number = int(data['alternate_mobile'])
		user_profile.blood_group = data['blood_group']

		address_obj = Address(address1=data['address_1'], city=data['city'], state=data['state'], pincode=data['pincode'], country=data['country'])
		if "address_2" in data and data['address_2'] != "" and data['address_2'] is not None:
			address_obj.address2 = data['address_2']
		address_obj.save()

		user_profile.address = address_obj
		user_profile.save()

		messages.success(request, "User successfully created.")

	return render(request, 'user_reg.html')


def user_login(request):
	if request.POST is not None and request.POST != {}:

		email = request.POST['email']
		password = request.POST['password']

		user_q = User.objects.filter(email=email)
		if user_q.exists():
			user_obj = user_q.first()
			username = user_obj.username
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				messages.success(request, "Logged In successfully")
				return redirect('/')
		else:
			messages.error(request, "User does not exists.")
			return render(request, 'base.html')

	return render(request, 'base.html')


def user_logout(request):
	logout(request)
	return render(request, 'base.html')

def hospital_registration(request):
	return render(request, 'hospital_reg.html')
