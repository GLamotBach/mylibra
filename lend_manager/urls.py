"""URL patterns for lend_manager"""

from django.urls import path
from . import views

app_name = 'lend_manager'
urlpatterns = [
    path('lend_request/<int:copy_id>/', views.lend_request_view, name='lend_request'),
    path('lend_overview/', views.lend_overview_view, name='lend_overview'),
    path('lend_accept/<int:lend_request_id>/', views.lend_accept_view, name='lend_accept'),
    path('book_returned/<int:lend_copy_id>/', views.book_return_view, name='book_returned'),
    path('confirmation/<int:lend_copy_id>/', views.book_return_confirmation_view, name='return_confirmation'),
]
