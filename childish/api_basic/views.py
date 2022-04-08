from .models import UserCar, CarBrand, CarModel, Account
from .serializers import AccountSerializer, UserCarSerializer, CarBrandSerializer, CarModelSerializer, RegistrationSerializer
from rest_framework.response import  Response
from rest_framework import generics, mixins, status
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


class BrandsGeneric(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()

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


class ModelsGeneric(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()

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


class RegistrationView(APIView):

    def get(self, request):
        data = {'instructions': 'please register by submitting the following information', 'email': '',
                'username': '', 'first_name': '', 'age': '', 'driving_license_exp_date': ''}

        return Response(data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['age'] = account.age
            data['driving_license_exp_date'] = account.driving_license_exp_date
        else:
            data = serializer.errors
        return Response(data)