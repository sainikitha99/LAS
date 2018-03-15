from django.conf.urls import url

from core.views import *

CORE_URLS = [
	url(r'^$', index, name='index'),
	url(r'^about/',about, name='about'),
    url(r'^overview/',overview, name='overview'),
    url(r'^contact/',contact, name='contact'),
    
    url(r'^hospital/dashboard/',hospital_dashboard, name='hospital_dashboard'),
    url(r'^hospital/requests/',hospital_requests, name='hospital_requests'),
    url(r'^hospital/feedback/',hospital_feedback, name='hospital_feedback'),
    url(r'^hospital/notifications/',hospital_notifications, name='hospital_notifications'),

    url(r'^user/dashboard/',user_dashboard, name='user_dashboard'),
    url(r'^user/requests/',user_requests, name='user_requests'),
    url(r'^user/raiserequest/',raise_request, name='raise_request'),
    url(r'^user/feedback/',user_feedback, name='user_feedback'),

]
