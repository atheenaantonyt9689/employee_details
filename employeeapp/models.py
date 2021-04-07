from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=300)
    
    designation= models.CharField(max_length=300)
    email= models.EmailField(max_length=254)
    contact_number=models.CharField(max_length=10)


    def __str__(self):        
       return self.name
