from django import forms

from . models import LendRequest

class LendRequestForm(forms.ModelForm):
    class Meta:
        model = LendRequest
        fields = []
        labels = {}