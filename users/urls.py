from django.urls import path
from .views import UserRegisterationView, UserLoginView


urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login')
]
