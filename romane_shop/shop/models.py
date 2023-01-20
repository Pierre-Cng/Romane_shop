from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=255)
    weight = models.FloatField()
    color = models.CharField(max_length=255)
    material = models.CharField(max_length=255)

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    address_street = models.CharField(max_length=255)
    address_zipcode = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_contry = models.CharField(max_length=255)

class Command(models.Model):
    command_number = models.IntegerField()
    items = models.CharField(max_length=255)
    payed = models.BooleanField(default=False)
    customer_email = models.EmailField()
