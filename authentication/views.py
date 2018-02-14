# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from authentication.models import UserRequest



def get_user_requests(request):
	requests = UserRequest.objects.filter(user_id=request.user.id)


def user_registration(request):
	requests = UserRequest.objects.all()
	context = {"requests": requests}
	return render(request, 'user_reg.html', context)
