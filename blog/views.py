from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from.models import Company, Country, Laptop, Food, Phone
from .forms import CompanyForm, CountryForm, LaptopForm, FoodForm, PhoneForm

def company(request):
    comp=Company.objects.all()
    return render(request, 'company.html', context={"comp":comp})

def read_company(request, id):
    comp=Company.objects.get(id=id)
    return render(request, 'read_company.html', context={"comp":comp})


def create_company(request):
    form=CompanyForm()
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/company')
    return render(request, 'create_company.html', context={"form":form})

    
def update_company(request, id):
    comp=Company.objects.get(id=id)
    form=CompanyForm(instance=comp)
    if request.method=='POST':
        form=CompanyForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
          
            return redirect('/company')
    
    return render(request, 'create_company.html', context={"form":form})

        

def delete_company(request, id):
    comp=get_object_or_404(Company, id=id)
    comp.delete()
    return redirect('/company')

############################# Country

def country(request):
    count=Country.objects.all()
    return render(request, 'country.html', context={"count":count})

def read_country(request, id):
    count=Country.objects.get(id=id)
    return render(request, 'read_country.html', context={"count":count})


def create_country(request):
    form=CountryForm()
    if request.method=='POST':
        form=CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/country')
    return render(request, 'create_country.html', context={"form":form})

    
def update_country(request, id):
    count=Country.objects.get(id=id)
    form=CountryForm(instance=count)
    if request.method=='POST':
        form=CountryForm(request.POST, instance=count)
        if form.is_valid():
            form.save()
          
            return redirect('/country')
    
    return render(request, 'create_country.html', context={"form":form})

        

def delete_country(request, id):
    count=get_object_or_404(Country, id=id)
    count.delete()
    return redirect('/country')
       
       
       
######################################## LATOP

def laptop(request):
    computer=Laptop.objects.all()
    return render(request, 'laptop.html', context={"computer":computer})

def read_laptop(request, id):
    computer=Laptop.objects.get(id=id)
    return render(request, 'read_laptop.html', context={"computer":computer})


def create_laptop(request):
    form=LaptopForm()
    if request.method=='POST':
        form=LaptopForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/laptop')
    return render(request, 'create_laptop.html', context={"form":form})

    
def update_laptop(request, id):
    computer=Laptop.objects.get(id=id)
    form=LaptopForm(instance=computer)
    if request.method=='POST':
        form=LaptopForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
          
            return redirect('/laptop')
    
    return render(request, 'create_laptop.html', context={"form":form})

        

def delete_laptop(request, id):
    computer=get_object_or_404(Laptop, id=id)
    computer.delete()
    return redirect('/laptop')
              
              
##################### FOOD



def food(request):
    meal=Food.objects.all()
    return render(request, 'food.html', context={"meal":meal})

def read_food(request, id):
    meal=Food.objects.get(id=id)
    return render(request, 'read_food.html', context={"meal":meal})


def create_food(request):
    form=FoodForm()
    if request.method=='POST':
        form=FoodForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/food')
    return render(request, 'create_food.html', context={"form":form})

    
def update_food(request, id):
    meal=Food.objects.get(id=id)
    form=FoodForm(instance=meal)
    if request.method=='POST':
        form=FoodForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
          
            return redirect('/food')
    
    return render(request, 'create_food.html', context={"form":form})

        

def delete_food(request, id):
    computer=get_object_or_404(Food, id=id)
    computer.delete()
    return redirect('/food')
              
############################ PHONE     

def phone(request):
    mobile=Phone.objects.all()
    return render(request, 'phone.html', context={"mobile":mobile})

def read_phone(request, id):
    mobile=Phone.objects.get(id=id)
    return render(request, 'read_phone.html', context={"mobile":mobile})


def create_phone(request):
    form=PhoneForm()
    if request.method=='POST':
        form=PhoneForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/phone')
    return render(request, 'create_phone.html', context={"form":form})

    
def update_phone(request, id):
    mobile=Phone.objects.get(id=id)
    form=PhoneForm(instance=mobile)
    if request.method=='POST':
        form=PhoneForm(request.POST, instance=mobile)
        if form.is_valid():
            form.save()
          
            return redirect('/phone')
    
    return render(request, 'create_phone.html', context={"form":form})

        

def delete_phone(request, id):
    mobile=get_object_or_404(Phone, id=id)
    mobile.delete()
    return redirect('/phone')