import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *
import random, datetime

studenti = Student.objects.all()
ucitelia = Ucitel.objects.all()
dnesny_rok = datetime.date.today().year

def ziskaj_datum(vek):
    mesiac = random.randint(1,12)
    rok_narodenia  = dnesny_rok - vek
    if mesiac == "1" or "3" or "5" or "7" or "8" or "10" or "12":
        den = random.randint(1,31)
    elif mesiac == "2":
        if rok_narodenia/4 == 0:
            den = random.randint(1,29) 
        else:
            den = random.randint(1,28)
    else:
        den = random.randint(1,30)
    return f"{den}.{mesiac}. {rok_narodenia}"

for i in studenti:
    if i.trieda.nazov[0] == "1":
        vek = 16
    elif i.trieda.nazov[0] == "2":
        vek = 17
    elif i.trieda.nazov[0] == "3":
        vek = 18
    elif i.trieda.nazov[0] == "4":
        vek = 19
    i.vek = vek
    i.rok_narodenia = dnesny_rok - vek
    i.datum_narodenia = ziskaj_datum(vek)
    i.save()
    
for j in ucitelia:
    vek = random.randint(25,61)
    j.vek = vek
    j.rok_narodenia = dnesny_rok - vek
    j.datum_narodenia = ziskaj_datum(vek)
    j.save()