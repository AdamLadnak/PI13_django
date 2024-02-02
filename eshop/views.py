from django.shortcuts import render
from . models import *

def show_all(request):
    categories = Category.objects.all().order_by("name")
    products = Product.objects.all().order_by("name")
    return render(request, "eshop/index.html", {"categories":categories, "products":products})

def show_categories(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "eshop/index.html", {"categories":categories})

def show_products(request, product):
    product_obj = Product.objects.get(name=product)

    return render(request, "eshop/product.html", {"product":product_obj})

def show_customers(request):
    customers = Customer.objects.all().order_by("surname")
    return render(request, "eshop/index.html", {"customers":customers})

def show_orders(request):
    orders = Order.objects.all()
    return render(request, "eshop/index.html", {"orders":orders})

def show_category(request, category):
    category_obj = Category.objects.get(name=category)
    products = Product.objects.filter(category_id=category_obj.pk).order_by("name")
    products_list = []
    for product in products:
        products_list.append(f"{product.name} {product.price}")
    return render(request, "eshop/product_list.html", {"category":category ,"products":products})
