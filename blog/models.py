from django.db import models

# Create your models here.
class Country(models.Model):
    capital_city=models.CharField(max_length=100)
    population=models.IntegerField()
    language=models.CharField(max_length=100)
    image=models.ImageField(null=True, upload_to='country_images/')
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.capital_city}"
    
   

class  Food(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
    
class Phone(models.Model):
    model=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):  
            return f"{self.model}"
        




class Laptop(models.Model):
    model=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
            return f"{self.model}"
        


class Company(models.Model):
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
   
   
    def __str__(self):
        return f"{self.company_name}"
