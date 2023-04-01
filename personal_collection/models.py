from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BookTitle(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200) #Dodać podpowiedzi istniejacych w bazie autorów
    genre = models.CharField(max_length=50, blank=True) #Zmienic na choice z wyborem gatunków, albo podpowiedzi
    isbn_nr = models.CharField(max_length=17, blank=True) #Dodać-walidator numeru, API czy coś
    language = models.CharField(max_length=20, blank=True) #Dodac domyslny wybór jako polski
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Zwraca reprezentacje modelu w formie tytułu książki"""
        return self.title #To widac w panelu admina

class BookCopy(models.Model):
    book_title = models.ForeignKey(BookTitle, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Informacje dodatkowe przydatne podczas zarzadzania modelem"""
        verbose_name_plural = 'BookCopies' #Zmienia sposób w jaki sposob django bedzie sie odnosił do wielu obiektów

    def __str__(self):
        """Zwraca reprezentacje modelu w formie tytułu ksiązki"""
        return f"{self.book_title}" #Tu dodac jeszcze nazwe wlasciciela