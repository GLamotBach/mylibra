from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import UsersPublicProfile
from .forms import UsersPublicProfileForm
from friend_list.models import FriendList, FriendInvite
# Create your views here.

@login_required
def profile_setup_view(request):
    '''Strona wstępnego ustawienia publicznego profilu'''
    if request.method != 'POST':
        # Nie przekazano danych - tworzenie pustego formularza.
        form = UsersPublicProfileForm()

    else:
        # Przekazano dane za pomocą rządania POST - przetwarzanie danych.
        form = UsersPublicProfileForm(data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('personal_collection:index')

    # Wyświetlenie pustego formularza
    context = {'form': form}
    return render(request, 'public_profile/setup.html', context)

@login_required
def edit_profile_view(request):
    '''Strona z ustawieniami publicznego profilu'''
    profile = UsersPublicProfile.objects.get(user=request.user)

    # Sprawdzenie czy profil należy do bieżącego użytkownika
    if profile.user != request.user:
        raise Http404

    if request.method != 'POST':
        # Wypełnienie formularza aktualną treścią.
        form = UsersPublicProfileForm(instance=profile)

    else:
        # Przekazano zmienione dane - przetwarzanie ich.
        form = UsersPublicProfileForm(request.POST, request.FILES, instance=profile,)
        if form.is_valid():
            form.save()
            return redirect('personal_collection:index')

    context = {'profile': profile, 'form': form,}
    return render(request, 'public_profile/edit_profile.html', context)

@login_required
def profile_view(request, profile_id):
    """Users public profile page"""
    profile = UsersPublicProfile.objects.get(id=profile_id)

    own_profile = False
    already_friend = False
    invitation_pending = False
    invitation_to_accept = False
    # Check if profile page belongs to the request user
    if profile.user == request.user:
        own_profile = True
    else:
        # Check if profile page belongs to a friend
        list_owner = UsersPublicProfile.objects.get(user_id=request.user)
        friends = FriendList.objects.filter(list_owner=list_owner, friend=profile_id)
        if friends.exists():
            already_friend = True
        else:
            # Check if owner of profile page has been invited to friends
            invitation_send = FriendInvite.objects.filter(from_user=list_owner, to_user=profile_id)
            if invitation_send.exists():
                invitation_pending = True
            else:
                invitation_received = FriendInvite.objects.filter(from_user=profile_id, to_user=list_owner)
                if invitation_received.exists():
                    invitation_to_accept = True


    context = {'profile': profile, 'own_profile': own_profile, 'already_friend': already_friend,
               'invitation_pending': invitation_pending, 'invitation_to_accept': invitation_to_accept,}
    return render(request, 'public_profile/profile.html', context)