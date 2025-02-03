from django.db import models

class Company(models.Model):
    compnay_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
