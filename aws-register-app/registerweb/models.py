from pyexpat import model
from django.db import models

class RegisterEmail(models.Model):
    emailid = models.EmailField(max_length=100, unique=True)

class Person(models.Model):
    name = models.CharField(max_length=50)