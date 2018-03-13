"""las URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

CORE_URLS = ""
AUTH_URLS = ""
from authentication.urls import *
from core.urls import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(AUTH_URLS)),
    url(r'^$', include(CORE_URLS)),
    url(r'^about/',about, name='about'),
    url(r'^overview/',overview, name='overview'),
    url(r'^contact/',contact, name='contact'),
    url(r'^dashboard/',dashboard, name='dashboard'),
    url(r'^requesth/',requesth, name='requesth'),
    url(r'^feedback/',feedback, name='feedback'),
    url(r'^notifications/',notifications, name='notifications'),

    url(r'^user_request/',user_request, name='user_request'),
    url(r'^my_requests/',my_requests, name='my_requests'),
    url(r'^give_feedback/',give_feedback, name='give_feedback'),
]
