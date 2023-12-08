from django.shortcuts import render
from . models import *

def vypis_post(request):
    posty = Post.objects.all().order_by("nadpis")
    return render(request, "blog/index.html", {"posty":posty})

def vypis_category(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "blog/index.html", {"categories":categories})

def vypis_autors(request):
    autors = Autors.objects.all().order_by("priezvisko")
    return render(request, "blog/index.html", {"autors":autors})