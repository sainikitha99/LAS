from django.conf.urls import url,include

from authentication.views import *

AUTH_URLS = [
	url(r'^register/user/', user_registration, name='user_registrations'),
	url(r'^user/login/', user_login, name='login'),
	url(r'^user/logout/', user_logout, name='user_logout'),
	url(r'^register/hospital/', hospital_registration, name='hospital_registrations'),
	url(r'^hospital/login/', hospital_login, name='login'),
	url(r'^hospital/logout/', hospital_logout, name='hospital_logout'),
	url(r'^auth/', include('social_django.urls', namespace='social')),

]
