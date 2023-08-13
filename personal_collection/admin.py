from django.contrib import admin

from .models import BookTitle, BookCopy

admin.site.register(BookTitle)
admin.site.register(BookCopy)
