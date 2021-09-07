#-*- coding:utf-8 -*-
from django.urls import path, re_path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.ApiRootView.as_view(), name='user_admin'),
]
