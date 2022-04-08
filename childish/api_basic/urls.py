from django.urls import path
from .views import UserCarAPIView, UserCarGeneric, AccountGeneric, BrandsAPIView, ModelsAPIView,\
    RegistrationView


urlpatterns = [
    path('usercars/', UserCarAPIView.as_view()),
    path('usercar/<int:id>/', UserCarGeneric.as_view()),
    path('brands/', BrandsAPIView.as_view()),
    path('models/', ModelsAPIView.as_view()),
    path('account/', AccountGeneric.as_view()),
    path('register/', RegistrationView.as_view(), name='register')
]