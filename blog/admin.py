from django.contrib import admin

# Register your models here.
from.models import Country
admin.site.register(Country)

from.models import Company
admin.site.register(Company)


from.models import Phone
admin.site.register(Phone)

from.models import Food
admin.site.register(Food)

from.models import Laptop
admin.site.register(Laptop)
