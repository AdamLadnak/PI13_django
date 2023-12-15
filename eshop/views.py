from django.shortcuts import render
from . models import *

def show_all(request):
    categories = Category.objects.all().order_by("name")
    products = Product.objects.all().order_by("name")
    customers = Customer.objects.all().order_by("surname")
    orders = Order.objects.all()
    return render(request, "eshop/index.html", {"categories":categories, "products":products, "customers":customers, "orders":orders})

def show_categories(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "eshop/index.html", {"categories":categories})

def show_products(request):
    products = Product.objects.all().order_by("name")
    return render(request, "eshop/index.html", {"products":products})

def show_customers(request):
    customers = Customer.objects.all().order_by("surname")
    return render(request, "eshop/index.html", {"customers":customers})

def show_orders(request):
    orders = Order.objects.all()
    return render(request, "eshop/index.html", {"orders":orders})
