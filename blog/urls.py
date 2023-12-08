from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_post, name='vypis-post'),
    path('categories/', views.vypis_category, name="vypis-category"),
    path('autors/', views.vypis_autors, name="vypis-autors"),
    
]