# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
	return render(request, 'base.html')

def overview(request):
	return render(request, 'overview.html')
def contact(request):
	return render(request, 'contact.html')
def about(request):
	return render(request, 'about.html')
