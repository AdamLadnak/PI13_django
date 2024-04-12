from django.shortcuts import render, HttpResponse
from . models import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    studenti = Student.objects.all().order_by("priezvisko")
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti, "kruzky":kruzky})
    
def vypis_students(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti })

def vypis_triedy(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy })

def vypis_ucitelov(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"ucitelia":ucitelia })

def vypis_kruzky(request):
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"kruzky":kruzky })

def vypis_trieda(request, trieda):
    trieda_obj = Trieda.objects.get(nazov=trieda)
    studenti = Student.objects.filter(trieda_id=trieda_obj.pk).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(f"{student.meno} {student.priezvisko}")
    ucitel = Ucitel.objects.get(trieda_id=trieda_obj.pk)
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"
    # return HttpResponse(f"{trieda}<br>{ucitel}<br>{studenti_list}")
    return render(request, "skola/trieda_list.html", {"trieda":trieda, "ucitel":ucitel, "studenti":studenti_list})

def vypis_ucitel(request, ucitel):
    ucitel = Ucitel.objects.get(id=ucitel)
    trieda = Trieda.objects.get(nazov=ucitel.trieda)
    try:
        kruzok = Kruzok.objects.get(ucitel = ucitel.pk)
    except:
        kruzok = ""
    return render(request, "skola/ucitel_detail.html", {"trieda":trieda, "ucitel":ucitel, "kruzok":kruzok})

def vypis_student(request, student):
    student = Student.objects.get(id=student)
    trieda = Trieda.objects.get(nazov = student.trieda)
    ucitel = Ucitel.objects.get(trieda = trieda.id)
    return render(request, "skola/student_detail.html", {"trieda":trieda, "ucitel":ucitel, "student":student})

def vypis_kruzok(request, kruzok):
    kruzok = Kruzok.objects.get(id=kruzok)
    ucitel = Ucitel.objects.get(kruzok=kruzok.id)
    studenti = Student.objects.filter(kruzok=kruzok.pk)
    return render(request, "skola/kruzok_detail.html", {"kruzok":kruzok, "ucitel":ucitel, "studenti":studenti})