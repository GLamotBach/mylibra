from django import forms

from .models import ReadBook, BookReview


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


