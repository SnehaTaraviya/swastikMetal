from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Getintouch(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'