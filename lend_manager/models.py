from django.db import models
from django.contrib.auth.models import User

from personal_collection.models import BookCopy

class LendRequest(models.Model):
    """Object storing a request for lending a book from one user to another"""
    requesting_user = models.ForeignKey(User, related_name='requesting_user', on_delete=models.CASCADE)
    copy_owner = models.ForeignKey(User, related_name='copy_owner', on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)

    def __str__(self):
        """Returns requesting user's id in admin panel"""
        return self.requesting_user


class LendCopy(models.Model):
    """Book copy that is currently being lended from the owner to another user"""
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    lend_start = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns copy owners id in admin panel"""
        return self.from_user



