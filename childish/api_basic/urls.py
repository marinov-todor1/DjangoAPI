from django.urls import path
from .views import UserCarAPIView, UserCarDetail, UserCarGeneric, AccountGeneric, \
    RegistrationView


urlpatterns = [
    path('usercar/', UserCarAPIView.as_view()),
    path('detail/<int:id>/', UserCarDetail.as_view()),
    path('generic/usercar/<int:id>/', UserCarGeneric.as_view()),
    path('generic/account/', AccountGeneric.as_view()),
    path('register/', RegistrationView.as_view(), name='register')
]