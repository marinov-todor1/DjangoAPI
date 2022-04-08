from django.urls import path
from .views import UserCarGeneric, AccountGeneric, ModelsGeneric,\
    RegistrationView, BrandsGeneric


urlpatterns = [
    path('usercars/', UserCarGeneric.as_view()),
    path('usercars/<int:id>/', UserCarGeneric.as_view()),
    path('brands/', BrandsGeneric.as_view()),
    path('brands/<int:id>/', BrandsGeneric.as_view()),
    path('models/<int:id>/', ModelsGeneric.as_view()),
    path('models/', ModelsGeneric.as_view()),
    path('accounts/', AccountGeneric.as_view()),
    path('accounts/<int:id>/', AccountGeneric.as_view()),
    path('register/', RegistrationView.as_view(), name='register')
]