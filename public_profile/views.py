from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import UsersPublicProfile
from .forms import UsersPublicProfileForm
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
def edit_profile_view(request, profile_id):
    '''Strona z ustawieniami publicznego profilu'''
    profile = UsersPublicProfile.objects.get(id=profile_id) # Do zmiany

    # Sprawdzenie czy profil należy do bieżącego użytkownika
    if profile.user != request.user:
        raise Http404

    if request.method != 'POST':
        # Wypełnienie formularza aktualną treścią.
        form = UsersPublicProfileForm(instance=profile)

    else:
        # Przekazano zmienione dane - przetwarzanie ich.
        form = UsersPublicProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_collection:index')