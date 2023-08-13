from django.contrib import admin

from .models import ReadBook, BookReview, BookRating

admin.site.register(ReadBook)
admin.site.register(BookReview)
admin.site.register(BookRating)
