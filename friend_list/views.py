from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import FriendList, FriendInvite
from .forms import FriendInviteForm, FriendListForm
from public_profile.models import UsersPublicProfile

@login_required
def friend_list_view(request):
    '''Strona wyświetlająca listę znajomych''' # Do przerobienia
    list_owner = UsersPublicProfile.objects.get(user_id=request.user)
    friends = FriendList.objects.filter(list_owner=list_owner.id).select_related("friend")
    context = {'friends': friends,}
    return render(request, 'friend_list/list.html', context)


@login_required
def friend_invite_view(request, profile_id): # Chyba można uprościć.
    '''Strona wysłania zaproszenia do znajomych'''
    invite_sender = UsersPublicProfile.objects.get(user_id=request.user)
    invited_user = UsersPublicProfile.objects.get(user_id=profile_id)
    # Check if users are not already friends
    already_friends = FriendList.objects.filter(list_owner=invite_sender.id, friend=invited_user.id)
    if already_friends.exists():
        raise Http404

    if request.method != 'POST':
        # Generowanie strony wysłania zaproszenia
        form = FriendInviteForm()

    else:
        form = FriendInviteForm(data=request.POST)
        if form.is_valid():
            invite = form.save(commit=False)  # Egzemplarz utworzony lecz nie zapisany w DB
            invite.from_user = invite_sender
            invite.to_user = invited_user
            invite.save()  # Zapisanie egzemplarza w DB
            return redirect('personal_collection:myshelf') # Tymczasowo

    # Wyświetlenie strony
    context = {'invited_user': invited_user, 'form': form,}
    return render(request, 'friend_list/send_invite.html', context)

@login_required
def invitation_list_view(request):
    '''Wyświetla bierzące zaproszenia'''
    profile = UsersPublicProfile.objects.get(user_id=request.user)
    # Zaproszenia przychodzące
    invitation_inbox = FriendInvite.objects.filter(to_user_id=profile.id).select_related("from_user")

    # Zaproszenia wychodzące
    invitation_outbox = FriendInvite.objects.filter(from_user_id=profile.id).select_related("to_user")

    # Przekazania danych do strony
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





