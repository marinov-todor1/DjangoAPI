from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import UserCar, CarBrand, CarModel
from .serializers import UserCarSerializer, CarBrandSerializer, CarModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
# Create your views here.


class UserCar_Generic(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserCarSerializer
    queryset = UserCar.objects.all()

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


class UserCar_APIView(APIView):

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


class UserCar_Detail(APIView):

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


@api_view(['GET', 'POST'])
def UserCar_list(request):

    if request.method == "GET":
        UserCars = UserCar.objects.all()
        serializer = UserCarSerializer(UserCars, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserCarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def UserCar_detail(request, pk):
    try:
        user_car = UserCar.objects.get(pk=pk)
    except UserCar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserCarSerializer(user_car)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserCarSerializer(user_car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user_car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


