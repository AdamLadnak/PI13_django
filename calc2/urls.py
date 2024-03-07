from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.calc2, name='calc2'),
]