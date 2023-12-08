from django.db import models
from django.utils import timezone

class Autors(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    nick = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.nick}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    autor = models.ForeignKey(Autors, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField()
    text = models.TextField()
    nadpis = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.autor} {self.create_date} {self.publish_date} {self.text} {self.nadpis}"


    


