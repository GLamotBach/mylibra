"""URL patterns for public_profile."""

from django.urls import path
from . import views

app_name = 'public_profile'
urlpatterns = [
    # Public profile initial setup page.
    path('setup/', views.profile_setup_view, name='setup'),
    # Profile information editing page.
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    # User's public profile page.
    path('<int:profile_id>/', views.profile_view, name='profile'),
    # User's public book collection.
    path('<int:profile_id>/collection>/', views.public_book_collection_view, name='public_collection'),
]