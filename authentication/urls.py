from django.conf.urls import url

from authentication.views import *

AUTH_URLS = [
	url(r'^register/user/', user_registration, name='user_registrations'),
	url(r'^registe/hospital/', hospital_registration, name='hospital_registrations'),
]
