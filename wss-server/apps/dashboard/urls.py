from django.urls import path
from . import views

urlpatterns = [
	path('', views.redirect_to_device, name='dashboard'),
	path('comming-soon/', views.ComingSoonView.as_view(), name='coming_soon'),
]
