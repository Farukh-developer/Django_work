from django import forms
from .models import Company, Country, Phone, Food, Laptop

class CompanyForm(forms.ModelForm):
    company_name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    location=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    
    class Meta:
        model=Company
        fields=('company_name','location')
 
#################        
        
class CountryForm(forms.ModelForm):
    capital_city=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    population=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    language=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    
    
    class Meta:
        model=Country
        fields=('capital_city','population','language', 'image')
        
############


class LaptopForm(forms.ModelForm):
    model=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    color=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    price=forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"number"}))
  
    
    
    class Meta:
        model=Laptop
        fields=('model','color','price')
        
################             


class FoodForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    country=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
   
  
    
    
    class Meta:
        model=Food
        fields=('name','country')                   
        
#####################   

class PhoneForm(forms.ModelForm):
    model=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    color=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    price=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    
   
    
    
    class Meta:
        model=Phone
        fields=('model','color','price')           