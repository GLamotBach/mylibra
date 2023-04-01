from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .models import BookCopy, BookTitle
from .forms import BookTitleForm, BooKCopyForm
# Create your views here.

def index(request):
    '''Strona główna aplikacji mylibra'''
    return render(request, 'personal_collection/index.html')

@login_required
def myshelf_view(request):
    '''Strona z listą wszystkich pozycji w kolekcji użytkownika'''
    books = BookCopy.objects.filter(owner=request.user).order_by('add_date')
    context = {'books': books}
    return render(request, 'personal_collection/myshelf.html', context)

@login_required
def copy_view(request, copy_id):
    '''Strona z szczegółowym opisem egzemplarza'''
    copy = BookCopy.objects.get(id=copy_id)
    title = BookTitle.objects.get(id=copy.book_title_id)
    # Sprawdzenie czy że obiekt należy do bieżącego użytkownika
    if copy.owner != request.user:
        raise Http404
    context = {'copy': copy, 'title': title}
    return render(request, 'personal_collection/copy.html', context)

@login_required
def new_title_view(request):
    '''Dodawanie nowego tytułu'''
    if request.method != 'POST':
        # Nie przekazano danych - tworzenie pustego formularza.
        form = BookTitleForm()
    else:
        # Przekazano dane za pomocą rządania POST - przetwarzanie danych.
        form = BookTitleForm(data=request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.added_by = request.user
            title.save()
            return redirect('personal_collection:add_to_collection', title_id=title.id)

    # Wyświetlenie pustego formularza
    context = {'form': form}
    return render(request, 'personal_collection/new_title.html', context)

@login_required
def add_to_collection_view(request, title_id):
    '''Dodanie książki do kolekcji'''
    title = BookTitle.objects.get(id=title_id)

    # Sprawdzenie czy że obiekt należy do bieżącego użytkownika - Rozwiązanie tymczasowe
    if title.added_by != request.user:
        raise Http404

    if request.method != 'POST':
        # Generowanie strony książki do dodania do kolekcji
        form = BooKCopyForm()
    else:
        # Zatwierdzenie książki do dodania
        form = BooKCopyForm(data=request.POST)
        if form.is_valid(): # Być może zbędne ale przyda się przy dalszym rozwoju
            add_book = form.save(commit=False) # Egzemplarz utworzony lecz nie zapisany w DB
            add_book.owner = request.user
            add_book.book_title = title # Przypisanie kolumnie book_title id książki
            add_book.save() # Zapisanie egzemplarza w DB
            return redirect('personal_collection:myshelf') # Docelowo do strony egzemplarza

    # Wyświetlenie strony
    context = {'title': title, 'form': form }
    return render(request, 'personal_collection/add_to_collection.html', context)

@login_required
def edit_title_view(request, copy_id):
    '''Edycja istniejącego tytułu'''
    copy = BookCopy.objects.get(id=copy_id)
    book = BookTitle.objects.get(id=copy.book_title_id)

    # Sprawdzenie czy że obiekt należy do bieżącego użytkownika
    if copy.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Wypełnienie formularza aktualną treścią.
        form = BookTitleForm(instance=book)
    else:
        # Przekazano zmienione dane - przetwarzanie ich.
        form = BookTitleForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_collection:copy', copy_id=copy_id)

    context = {'copy': copy, 'book': book, 'form': form,}
    return render(request, 'personal_collection/edit_title.html', context)