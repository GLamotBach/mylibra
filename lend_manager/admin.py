from django.contrib import admin

from .models import LendRequest, LendCopy

admin.site.register(LendRequest)
admin.site.register(LendCopy)
