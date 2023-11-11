from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, GenerateNewPasswordView, UserVerifyView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/verify/<int:pk>/', UserVerifyView.as_view(), name='verification'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', GenerateNewPasswordView.as_view(), name='generate_new_password'),

]
