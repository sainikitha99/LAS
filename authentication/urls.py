from django.conf.urls import url,include

from authentication.views import *

AUTH_URLS = [
	url(r'^register/user/', user_registration, name='user_registration'),
	url(r'^user/login/', login_view, name='login'),
	url(r'^user/logout/', logout_view, name='user_logout'),
	url(r'^register/hospital/', hospital_registration, name='hospital_registration'),
	url(r'^social_auth/', include('social_django.urls', namespace='social')),
	url(r'^user/profile/', view_profile, name='view_profile'),
	url(r'^userprofile/edit/', edit_profile, name='edit_profile'),
]
