from django.db import models


# Designing the database
class From(models.Model):
    first_name = models.CharField(max_length=80)  
    lastname = models.CharField(max_length=80) 
    email = models.EmailField(max_length=80)  
    date = models.DateField()  
    occupation = models.CharField(max_length=80)  

    
    def __str__(self):
        return f"{self.first_name} {self.lastname}"
