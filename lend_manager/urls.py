"""URL patterns for lend_manager"""

from django.urls import path
from . import views

app_name = 'lend_manager'
urlpatterns = [
    path('lend_request/<int:copy_id>/', views.lend_request_view, name='lend_request'),
    path('lend_overview/', views.lend_overview_view, name='lend_overview'),
]
