from django.contrib import admin
from django.urls import path, include

from .views import register_view, login_view, error_view, profile_view

urlpatterns = [
    path('registration/',register_view , name='registration'),
    path('login', login_view, name='login'),
    path('error', error_view, name='error' ),
    path('profile', profile_view, name='profile' ),
]
