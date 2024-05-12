from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import company, country, laptop , phone, food,read_company, create_company, update_company, delete_company, create_country,  read_country, update_country, delete_country, create_laptop, update_laptop, delete_laptop,read_laptop, create_food, read_food, update_food, delete_food, create_phone, update_phone, delete_phone, read_phone

urlpatterns = [
    path('company/', company, name='company_page'),
    path('read_company/<int:id>/', read_company, name='read_company'),
    path('create_company/', create_company, name='create_company'),
    path('update_company/<int:id>/', update_company, name='update_company'),
    path('delete_company/<int:id>/', delete_company, name='delete_company'),
    
    
    path('country/', country, name='country_page'),
    path('read_country/<int:id>/', read_country, name='read_country'),
    path('create_country/', create_country, name='create_country'),
    path('update_country/<int:id>/', update_country, name='update_country'),
    path('delete_country/<int:id>/', delete_country, name='delete_country'),
    
    
    path('laptop/', laptop, name='laptop_page'),
    path('read_laptop/<int:id>/', read_laptop, name='read_laptop'),
    path('create_laptop/', create_laptop, name='create_laptop'),
    path('update_laptop/<int:id>/', update_laptop, name='update_laptop'),
    path('delete_laptop/<int:id>/', delete_laptop, name='delete_laptop'),
    
    
    path('food/', food, name='food_page'),
    path('read_food/<int:id>/', read_food, name='read_food'),
    path('create_food/', create_food, name='create_food'),
    path('update_food/<int:id>/', update_food, name='update_food'),
    path('delete_food/<int:id>/', delete_food, name='delete_food'),
    
    
    path('phone/', phone, name='phone_page'),
    path('read_phone/<int:id>/', read_phone, name='read_phone'),
    path('create_phone/', create_phone, name='create_phone'),
    path('update_phone/<int:id>/', update_phone, name='update_phone'),
    path('delete_phone/<int:id>/', delete_food, name='delete_phone'),
    
    
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
