"""Definiuje wzorce URL dla personal_collection"""

from django.urls import path
from . import views

app_name = 'personal_collection'
urlpatterns = [
    # Strona główna.
    path('', views.index, name='index'),
    # Lista książek użytkownika
    path('myshelf/', views.myshelf_view, name='myshelf'),
    # Szczegółowy opis egzemplarza książki
    path('myshelf/(<int:copy_id>)/', views.copy_view, name='copy'),
    # Strona dodawania książki
    path('new_title/', views.new_title_view, name='new_title'),
    # Strona dodawania książki do prywatnej kolekcji
    path('add_to_collection/<int:title_id>)/', views.add_to_collection_view, name='add_to_collection'),
    # Strona edycji książki
    path('edit_title/<int:copy_id>/', views.edit_title_view, name='edit_title'),
]