from django.conf.urls import url

from core.views import *

CORE_URLS = [
	url(r'^$', index, name='index'),
]
