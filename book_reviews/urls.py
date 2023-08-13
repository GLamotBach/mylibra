"""URL patterns for book_reviews."""

from django.urls import path
from . import views


app_name = 'book_reviews'
urlpatterns = [
    # Page handling adding book to read list.
    path('read/(<int:title_id>)/', views.read_book_view, name='read_book'),
    # List of users read books.
    path('myreadlist/', views.my_read_books_list_view, name='my_read_list'),
    # Page for writing a new review.
    path('addreview/(<int:read_book_id>)/', views.add_review_view, name='add_review'),
    # Page for editing existing review.
    path('edit_review/(<int:read_book_id>)/', views.edit_review_view, name='edit_review'),
    # Page for rating a book.
    path('rate_book/(<int:read_book_id>)/', views.add_rating_view, name='rate_book'),
]