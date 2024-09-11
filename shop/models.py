from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=100)
    password = models.TextField(max_length=1000)
    emailid = models.CharField(max_length=1001)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    pname = models.CharField(max_length=100)
    pdesc = models.TextField(max_length=1000)
    stock = models.IntegerField(max_length=1000)
    pprice = models.IntegerField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/',null=True , blank=True)
    def __str__(self):
        return self.pname