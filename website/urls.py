from django.contrib import admin
from django.urls import path
from . import views
from . import services

urlpatterns = [
    path('', views.homeRequest, name='index'),
    path('start', services.reverse)
]
