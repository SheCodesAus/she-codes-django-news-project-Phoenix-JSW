from django.urls import path
from .views import CreateAccountView, profile, UpdateAccountView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account', CreateAccountView.as_view(), name='createAccount'),
    path('profile', profile, name='profile'),
    path('profile/userUpdate', UpdateAccountView.as_view(), name='userUpdate'),
    # path('author/<slug:slug>/, views.AuthorView.as_view(), name='authorDetail'),
]
