from django.contrib import admin

from .models import FriendList, FriendInvite

admin.site.register(FriendList)
admin.site.register(FriendInvite)
