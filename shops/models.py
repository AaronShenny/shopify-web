from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    cordinates =  models.IntegerField()
    state = models.CharField(max_length=100)
    adress = models.TextField()
    def __str__(self):
        return self.name

class Orders(models.Model):
    userid = models.IntegerField()
    orderid = models.IntegerField()
    orders = models.TextField()
    amount = models.IntegerField()
    location = models.TextField()
    top = models.CharField(max_length=100) #typeofpayment
    def __str__(self):
        return self.name
