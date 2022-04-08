from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

PRIMARY_DRIVER = (('Y', 'Yes'), ('N', 'No'))
ACCIDENTS_HISTORY = (('Y', 'Yes'), ('N', 'No'))
# Create your models here.


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class SoftDeleteUserModel(User):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Account(SoftDeleteUserModel):
    driver = models.CharField(max_length=3, choices=PRIMARY_DRIVER)
    accident_status = models.CharField(max_length=3, choices=ACCIDENTS_HISTORY)

    def __str__(self):
        return self.first_name


class CarBrand(SoftDeleteModel):
    brand_name = models.CharField(max_length=20)

    def __str__(self):
        return self.brand_name


class CarModel(SoftDeleteModel):
    name = models.CharField(max_length=20)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserCar(SoftDeleteModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    car_brand = models.ManyToManyField(CarBrand)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    first_reg = models.DateTimeField()
    odometer = models.IntegerField()

    def __str__(self):
        return self.user.first_name



