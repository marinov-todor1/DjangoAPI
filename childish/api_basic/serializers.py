from rest_framework import serializers
from .models import UserCar, CarBrand, CarModel


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ['id', 'user_name', 'car_brand', 'first_reg', 'odometer']


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'brand_name']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'brand']


