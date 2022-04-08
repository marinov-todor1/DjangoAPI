from rest_framework import serializers
from .models import UserCar, CarBrand, CarModel, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'driver', 'owner', 'first_name', 'email']


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ['id', 'user', 'car_brand', 'first_reg', 'odometer']


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'brand_name']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'brand']


class RegistrationSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'repeat_password', 'first_name']
        extra_kwargs = {
            'password ': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name']
        )
        password = self.validated_data['password']
        repeat_password = self.validated_data['repeat_password']

        if password != repeat_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
