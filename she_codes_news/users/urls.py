from django.urls import path
from .views import CreateAccountView, profile, UpdateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account', CreateAccountView.as_view(), name='createAccount'),
    path('profile', profile, name='profile'),
    path('profile/userUpdate', UpdateAccountView.as_view(), name='userUpdate'),
]
