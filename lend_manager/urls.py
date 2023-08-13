"""URL patterns for lend_manager."""

from django.urls import path
from . import views

app_name = 'lend_manager'
urlpatterns = [
    # Url for handling a new lend_request.
    path('lend_request/<int:copy_id>/', views.lend_request_view, name='lend_request'),
    # Page containing all lend requests and books being lend by and to the user.
    path('lend_overview/', views.lend_overview_view, name='lend_overview'),
    # Url for handling the accepting of a lend_request.
    path('lend_accept/<int:lend_request_id>/', views.lend_accept_view, name='lend_accept'),
    # Url for handling a return of a book to its owner.
    path('book_returned/<int:lend_copy_id>/', views.book_return_view, name='book_returned'),
    # Page for conforming that the book was returned.
    path('confirmation/<int:lend_copy_id>/', views.book_return_confirmation_view, name='return_confirmation'),
    # Url for handling the cancellation of lend_request by the issuing user.
    path('cancel/<int:lend_request_id>/', views.cancel_lend_request_view, name='cancel_request'),
    # Url for refusal of a lend_request by the book owner.
    path('refuse/<int:lend_request_id>/', views.refuse_lend_request_view, name='refuse_request'),
]
