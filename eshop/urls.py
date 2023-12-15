from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all, name='show-all'),
    path('categories/', views.show_categories, name="show-categories"),
    path('products/', views.show_products, name="show-products"),
    path('customers/', views.show_customers, name="show-customers"),
    path('orders/', views.show_orders, name="show-orders"),
    
]