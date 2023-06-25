from django.db import models
from django.contrib.auth.models import User
from public_profile.models import UsersPublicProfile

# Create your models here.
class FriendInvite(models.Model):
    from_user = models.ForeignKey(UsersPublicProfile, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UsersPublicProfile, related_name='to_user', on_delete=models.CASCADE)
    date_of_invite = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Zwraca id użytkownika który złożył zaproszenie"""
        return self.from_user

class FriendList(models.Model):
    list_owner = models.ForeignKey(UsersPublicProfile, related_name='list_owner', on_delete=models.CASCADE)
    friend = models.ForeignKey(UsersPublicProfile, related_name='friend', on_delete=models.CASCADE)
    friends_since = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Zwraca id użytkownika którego dotyczy znajomość"""
        return self.list_owner