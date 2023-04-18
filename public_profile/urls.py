"""Definiuje wzorce URL dla public_profile"""

from django.urls import path
from . import views

app_name = 'public_profile'
urlpatterns = [
    # Strona setupu profilu
    path('setup/', views.profile_setup_view, name='setup'),
]