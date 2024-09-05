from django.db import models

# Create your models here.
class CreateUser(models.Model):
    name = models.CharField(max_length=100)
    password = models.TextField(max_length=1000)
    emailid = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name