from django.db import models


# Create your models here.

class CarBrand(models.Model):
    brand_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.brand_name


class UserCar(models.Model):
    user_name = models.CharField(max_length=100)
    car_brand = models.ManyToManyField(CarBrand)
    first_reg = models.DateTimeField()
    odometer = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_name


class CarModel(models.Model):
    name = models.CharField(max_length=20)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
