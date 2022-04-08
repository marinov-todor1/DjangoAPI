
from .models import UserCar, CarBrand, CarModel, Account
from .serializers import AccountSerializer, UserCarSerializer, CarBrandSerializer, CarModelSerializer, RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AccountGeneric(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class UserCarGeneric(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    serializer_class = UserCarSerializer
    queryset = UserCar.objects.all()

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class UserCarAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        UserCars = UserCar.objects.all()
        serializer = UserCarSerializer(UserCars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCarDetail(APIView):

    def get_object(self, id):
        try:
            return UserCar.objects.get(id=id)
        except UserCar.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user_car = self.get_object(id)
        serializer = UserCarSerializer(user_car)
        return Response(serializer.data)

    def put(self, request, id):
        user_car = self.get_object(id)
        serializer = UserCarSerializer(user_car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user_car = self.get_object(id)
        user_car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegistrationView(APIView):

    def get(self, request):
        data = {'instructions': 'please register by submitting the following information', 'email': '',
                'username': '', 'first_name': '', 'driver': 'Y/N', 'ever_involved_in_accidents': 'Y/N'}

        return Response(data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)
