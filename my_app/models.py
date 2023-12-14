from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
