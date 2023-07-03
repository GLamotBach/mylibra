"""URL patterns for book_reviews"""

from django.urls import path
from . import views


app_name = 'book_reviews'
urlpatterns = [
    path('read/(<int:title_id>)/', views.read_book_view, name='read_book'),
    path('myreadlist/', views.my_read_books_list_view, name='my_read_list'),
    path('addreview/(<int:read_book_id>)/', views.add_review_view, name='add_review'),
    path('edit_review/(<int:book_review_id>)/', views.edit_review_view, name='edit_review'),
]