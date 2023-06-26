"""URL patterns for friend_list"""

from django.urls import path
from . import views

app_name = 'friend_list'
urlpatterns = [
    # Page containing the list of friends
    path('list/', views.friend_list_view, name='friendlist'),
    # Confirmation of sending the invitation
    path('invite/<int:profile_id>/', views.friend_invite_view, name='invite'),
    # List of pending, send and received invitations
    path('invitations/', views.invitation_list_view, name='invitations'),
    # Accepting invitation to friend list
    path('confirm/<int:profile_id>/', views.invitation_accept_view, name='accept_invite'),
]