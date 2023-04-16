from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UsersPublicProfile
from .forms import UsersPublicProfileForm
# Create your views here.

@login_required
def edit_profile_view(request):
    '''Strona z ustawieniami publicznego profilu'''