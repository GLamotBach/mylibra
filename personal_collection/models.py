from django.db import models
from django.contrib.auth.models import User


class BookTitle(models.Model):
    """Information about a book title."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, blank=True)
    isbn_nr = models.CharField(max_length=17, blank=True)
    language = models.CharField(max_length=20, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='images/', null=True, default='images/placeholder_cover.png',)

    def __str__(self):
        """Displays book title in the admin panel."""
        return self.title


class BookCopy(models.Model):
    """Specific copy of a book title."""
    book_title = models.ForeignKey(BookTitle, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Additional information useful for managing the model."""
        verbose_name_plural = 'BookCopies'

    def __str__(self):
        """Displays book copy title in the admin panel."""
        return f"{self.book_title}"