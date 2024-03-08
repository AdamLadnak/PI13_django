from django.shortcuts import render
import random
from calc2.models import *

def testovac(request):
    global priklad
    

    if request.method == "GET":
        priklady = Priklad.objects.all()
        priklad = random.choice(priklady)
        return render(request, "testovac/index.html", {"priklad": priklad})

    else:
        try: 
            vysledok = float(request.POST["vysledok"])
        except:
            vysledok = "Zadaj čísla"
            return render(request, "testovac/index.html", {"vysledok":vysledok, "priklad": priklad})

        if vysledok == float(priklad.vysledok):
            vysledok = "Správne!!!"
            return render(request, "testovac/index.html", {"vysledok":vysledok, "priklad": priklad})

        else:
            vysledok = "Lenka sa zamračila"

        return render(request, "testovac/index.html", {"vysledok":vysledok, "priklad": priklad})