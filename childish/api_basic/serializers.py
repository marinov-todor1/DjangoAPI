from rest_framework import serializers
from .models import UserCar, CarBrand, CarModel, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'age', 'driving_license_exp_date', 'first_name', 'email']


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ['id', 'user', 'car_brand', 'car_model', 'first_reg', 'odometer']


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
        fields = ['username', 'email', 'password', 'repeat_password', 'first_name', 'age', 'driving_license_exp_date']
        extra_kwargs = {
            'password ': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            age=self.validated_data['age'],
            driving_license_exp_date=self.validated_data['driving_license_exp_date']
        )
        password = self.validated_data['password']
        repeat_password = self.validated_data['repeat_password']

        if password != repeat_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
