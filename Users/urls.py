from Users import views

__author__ = 'NoahButler'

from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.login_page),
    url(r'^signup/$', views.signup_page),
    url(r'^create-group/$', views.create_new_group),
]


