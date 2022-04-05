from django.urls import path
from .views import UserCar_list, UserCar_detail, UserCar_APIView, UserCar_Detail, UserCar_Generic


urlpatterns = [
    path('usercar/', UserCar_APIView.as_view()),
    path('detail/<int:id>/', UserCar_Detail.as_view()),
    path('generic/usercar/<int:id>/', UserCar_Generic.as_view())
]