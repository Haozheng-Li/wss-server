#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2023/2/1 16:01
# @Author : Haozheng Li (Liam)
# @Email : haozheng.l@outlook.com


from django.urls import path
from . import views
from apps.devices.views import DeviceListView

urlpatterns = [
	path('', views.redirect_to_device, name='dashboard'),
	path('comming-soon/', views.ComingSoonView.as_view(), name='coming_soon'),
]