from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='skola'),
    path('triedy/', views.vypis_triedy, name="triedy"),
    path('ucitelia/', views.vypis_ucitelov, name="ucitelia"),
    path('studenti/', views.vypis_students, name="studenti"),
    path('kruzky/', views.vypis_kruzky, name="kruzky"),
    path('triedy/<trieda>/', views.vypis_trieda, name='trieda'),
    path('studenti/<student>/', views.vypis_student, name='student'),
    path('kruzky/<kruzok>/', views.vypis_kruzok, name='kruzok'),
]