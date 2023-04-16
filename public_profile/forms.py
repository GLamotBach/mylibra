from django import forms

from .models import UsersPublicProfile

class UsersPublicProfileForm(forms.ModelForm):
    class Meta:
        model = UsersPublicProfile
        fields = ['public_name',]
        labels = {'public_name': 'Nazwa użytkownika',}
