from django.db import models

class Enquiry(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.IntegerField(unique=True)
    address=models.TextField()
    branch=models.CharField(max_length=20)
    date=models.DateField()


