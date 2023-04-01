"""Definicje wzorców adresów URL aplikacji users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Domyślne adresy URL uwierzytelnienia
    path('', include('django.contrib.auth.urls')),
    # Strona rejestracji
    path('register', views.register, name='register'),
]