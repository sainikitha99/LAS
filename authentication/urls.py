from django.conf.urls import url

from authentication.views import *

AUTH_URLS = [
	url(r'^user_registration/', user_registration, name='user_registrations'),
	url(r'^get_requests/', get_user_requests, name='user_requests'),
	url(r'^main_page/', main_page, name='main_page'),
]
