from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)