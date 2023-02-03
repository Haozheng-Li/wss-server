#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022/12/27 16:47
# @Author : Haozheng Li (Liam)
# @Email : haozheng.l@outlook.com

from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register_success/', views.RegisterSuccess.as_view(), name='register_success'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
]
