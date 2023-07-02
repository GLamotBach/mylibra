from django.db import models
from django.contrib.auth.models import User

from personal_collection.models import BookTitle


class ReadBook(models.Model):
    """Book marked by user as already read"""
    book_title = models.ForeignKey(BookTitle, on_delete=models.PROTECT)
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Displays book title in the admin panel"""
        return self.book_title


class BookReview(models.Model):
    """Book review added by user"""
    read = models.ForeignKey(ReadBook, on_delete=models.CASCADE)
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    review = models.TextField(max_length=5000, null=True)

    def __str__(self):
        """Displays the user and the reviewed book in admin panel"""
        return f"{self.user}: {self.title}"


class BookRating(models.Model):
    """Rating of a book by an user"""
    book = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)

    def __str__(self):
        """Displays book and reader who added the rating in the admin panel"""
        return f"{self.post.book}: {self.reader}"