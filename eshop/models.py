from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=155) 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return f"{self.name} {self.category} {self.price} {self.description}"

class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Order(models.Model):
    cislo = models.DecimalField(decimal_places=0, max_digits=4, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.cislo} {self.customer} {self.order} {self.date}"