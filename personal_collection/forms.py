from django import forms

from .models import BookTitle, BookCopy

class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ['title', 'author', 'genre', 'isbn_nr', 'language',]
        labels = {'title': 'Tytuł',
                  'author': 'Autor',
                  'genre': 'Gatunek',
                  'isbn_nr': 'ISBN',
                  'language': 'Język',}

class BooKCopyForm(forms.ModelForm):
    class Meta:
        model = BookCopy
        fields = []
        labels = {}