"""URL patterns for friend_list."""

from django.urls import path
from . import views

app_name = 'friend_list'
urlpatterns = [
    # Page containing the list of friends.
    path('list/', views.friend_list_view, name='friendlist'),
    # Confirmation of sending the invitation.
    path('invite/<int:profile_id>/', views.friend_invite_view, name='invite'),
    # List of pending, send and received invitations.
    path('invitations/', views.invitation_list_view, name='invitations'),
    # Accepting invitation to friend list.
    path('confirm/<int:profile_id>/', views.invitation_accept_view, name='accept_invite'),
    # Rejecting invitation to friend list.
    path('reject/<int:profile_id>/', views.invitation_reject_view, name='reject_invite'),
    # Canceling invitation issued by the user.
    path('cancel/<int:profile_id>/', views.invitation_cancel_view, name='cancel_invite'),
    # Search for users.
    path('search/', views.user_search_view, name='user_search'),
]