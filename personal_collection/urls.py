"""URL patterns for personal_collection"""

from django.urls import path
from . import views

app_name = 'personal_collection'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # List of books belonging to the user
    path('myshelf/', views.myshelf_view, name='myshelf'),
    # Detailed information about the book copy
    path('myshelf/(<int:copy_id>)/', views.copy_view, name='copy'),
    # Detailed information about the book title
    # Nie bangala
    path('title/(<int:title_id>)/', views.title_view, name='title'),
    # Page for adding a new book title
    path('new_title/', views.new_title_view, name='new_title'),
    # Page for adding a new book copy to user's collection
    path('add_to_collection/<int:title_id>)/', views.add_to_collection_view, name='add_to_collection'),
    # Page for editing a book title
    path('edit_title/<int:copy_id>/', views.edit_title_view, name='edit_title'),
    # Copy search results
    path('copy_search/', views.copy_search_view, name='copy_search'),
    # Title search results
    path('title_search/', views.title_search_view, name='title_search'),
]