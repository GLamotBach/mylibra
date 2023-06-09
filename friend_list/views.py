from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import FriendList, FriendInvite
from .forms import FriendInviteForm, FriendListForm
from public_profile.models import UsersPublicProfile


@login_required
def friend_list_view(request):
    """Page displaying the friend list"""
    list_owner = UsersPublicProfile.objects.get(user_id=request.user)
    friends = FriendList.objects.filter(list_owner=list_owner.id).select_related("friend")
    context = {'friends': friends,}
    return render(request, 'friend_list/list.html', context)


@login_required
def friend_invite_view(request, profile_id):
    """Page for sending friend invitation"""
    invite_sender = UsersPublicProfile.objects.get(user_id=request.user)
    invited_user = UsersPublicProfile.objects.get(user_id=profile_id)

    # Check if users are not already friends
    already_friends = FriendList.objects.filter(list_owner=invite_sender.id, friend=invited_user.id)
    if already_friends.exists():
        raise Http404

    if request.method != 'POST':
        form = FriendInviteForm()

    else:
        form = FriendInviteForm(data=request.POST)
        if form.is_valid():
            invite = form.save(commit=False)
            invite.from_user = invite_sender
            invite.to_user = invited_user
            invite.save()
            return redirect('friend_list:invitations')

    context = {'invited_user': invited_user, 'form': form,}
    return render(request, 'friend_list/send_invite.html', context)


@login_required
def invitation_list_view(request):
    """Lists of pending invitation, send and received"""
    profile = UsersPublicProfile.objects.get(user_id=request.user)
    # Received invitations
    invitation_inbox = FriendInvite.objects.filter(to_user_id=profile.id).select_related("from_user")

    # Send invitations
    invitation_outbox = FriendInvite.objects.filter(from_user_id=profile.id).select_related("to_user")

    context = {'inbox': invitation_inbox, 'outbox': invitation_outbox,}
    return render(request, 'friend_list/invitations.html', context)


@login_required
def invitation_accept_view(request, profile_id):
    """Adds new rows to FriendList and deletes invitation from FriendInvite"""
    accepting_user = UsersPublicProfile.objects.get(user_id=request.user)
    accepted_user = UsersPublicProfile.objects.get(id=profile_id)
    invitation = FriendInvite.objects.get(to_user=accepting_user.id, from_user=profile_id)

    # Creating row for accepting user in FriendList table
    form = FriendListForm()
    accept = form.save(commit=False)
    accept.list_owner = accepting_user
    accept.friend = accepted_user
    accept.save()

    # Creating row for invitation sender in FriendList table
    form = FriendListForm()
    sender = form.save(commit=False)
    sender.list_owner = accepted_user
    sender.friend = accepting_user
    sender.save()

    # Deleting accepted invitation
    invitation.delete()
    context = {'accepted_user': accepted_user,}
    return render(request, 'friend_list/confirmation.html', context)


@login_required
def user_search_view(request):
    """Shows the results of searching for users"""
    if request.method == 'POST':
        search_query = request.POST["search_query"]
        results = UsersPublicProfile.objects.filter(public_name__icontains=search_query)
        context = {'query': search_query, 'results': results,}
    else:
        context = {}
    return render(request, 'friend_list/search.html', context)







