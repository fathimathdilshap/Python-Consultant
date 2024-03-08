from django.db import models

# Create your models here.
class regtable(models.Model):
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    Gender=models.CharField(max_length=10)
    Adrs=models.TextField()
    Mobnum=models.IntegerField()
    Pin=models.IntegerField()
    Username=models.CharField(max_length=25)
    Password=models.CharField(max_length=25)




