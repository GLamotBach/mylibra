from django.contrib import admin

# Register your models here.

from .models import BookTitle, BookCopy

admin.site.register(BookTitle)
admin.site.register(BookCopy)
