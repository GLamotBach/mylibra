from django import forms

from .models import ReadBook, BookReview, BookRating


class ReadBookForm(forms.ModelForm):
    class Meta:
        model = ReadBook
        fields = []
        labels = {}

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['review']
        labels = {'review': 'Recenzja'}

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ['rating']
        labels = {'rating': 'Ocena'}


