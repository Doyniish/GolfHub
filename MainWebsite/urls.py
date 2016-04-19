from MainWebsite import views

__author__ = 'NoahButler'

from django.conf.urls import url

urlpatterns = [
    url(r'^home/$', views.home_page),
]
