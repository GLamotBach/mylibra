from django.db import models
from public_profile.models import UsersPublicProfile


class FriendInvite(models.Model):
    """Invitation to join a friend list"""
    from_user = models.ForeignKey(UsersPublicProfile, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UsersPublicProfile, related_name='to_user', on_delete=models.CASCADE)
    date_of_invite = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns inviting user's id in admin panel"""
        return self.from_user


class FriendList(models.Model):
    """Contains information about a friend relation between two users"""
    list_owner = models.ForeignKey(UsersPublicProfile, related_name='list_owner', on_delete=models.CASCADE)
    friend = models.ForeignKey(UsersPublicProfile, related_name='friend', on_delete=models.CASCADE)
    friends_since = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the id of friend list owner"""
        return self.list_owner