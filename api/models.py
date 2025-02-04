from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)  # Fixed typo
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name  

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)  # Using EmailField for validation
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")  # Added related_name

    def __str__(self):
        return f"{self.name} - {self.position}"  
