from django.contrib import admin
from .models import UserCar, CarBrand, CarModel

# Register your models here.
admin.site.register(UserCar)
admin.site.register(CarModel)
admin.site.register(CarBrand)