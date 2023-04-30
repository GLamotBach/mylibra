from django import forms

from .models import UsersPublicProfile

class UsersPublicProfileForm(forms.ModelForm):
    class Meta:
        model = UsersPublicProfile
        fields = ['public_name', 'location', 'bio', 'image',]
        labels = {'public_name': 'Nazwa użytkownika',
                  'location': 'Lokacja',
                  'bio': 'Bio',
                  'image': 'Zdjęcie profilowe',
                  }
