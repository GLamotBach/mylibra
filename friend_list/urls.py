"""Definiuje wzorce URL dla friend_list"""

from django.urls import path
from . import views

app_name = 'friend_list'
urlpatterns = [
    # Lista znajomych
    path('list/', views.friend_list_view, name='friendlist'),
    path('invite/<int:profile_id>/', views.friend_invite_view, name='invite'),
    path('invitations/', views.invitation_list_view, name='invitations'),
    path('confirm/<int:profile_id>/', views.invitation_accept_view, name='accept_invite'),
]