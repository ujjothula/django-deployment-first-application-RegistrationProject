from django.db import models

# Create your models here.
class Registration(models.Model):
    Registrationdate=models.DateField()
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    rating = models.FloatField()
