from django import forms

from .models import FriendInvite, FriendList

class FriendInviteForm(forms.ModelForm):
    class Meta:
        model = FriendInvite
        fields = []
        labels = {}

class FriendListForm(forms.ModelForm):
    class Meta:
        model = FriendList
        fields = []
        labels = {}