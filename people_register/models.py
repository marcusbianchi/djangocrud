from django.db import models

# Create your models here.
class People(models.Model):
    person =models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=30)