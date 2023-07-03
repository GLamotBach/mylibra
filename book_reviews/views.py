from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from personal_collection.models import BookTitle
from .forms import ReadBookForm, BookReviewForm
from .models import ReadBook, BookReview

@login_required
def read_book_view(request, title_id):
    """View for handling adding book to read list"""
    book = BookTitle.objects.get(id=title_id)
    user = request.user

    form = ReadBookForm()
    read_book = form.save(commit=False)
    read_book.book_title = book
    read_book.reader = user
    read_book.save()

    return redirect('personal_collection:title', title_id=title_id)


@login_required
def my_read_books_list_view(request):
    """List of books user marked as read"""
    read_books = ReadBook.objects.filter(reader=request.user)
    reviewed_books = BookReview.objects.filter(user=request.user).values_list("read", flat=True)
    reviews = BookReview.objects.filter(user=request.user)

    context = {'read_books': read_books, 'reviewed_books': reviewed_books, 'reviews': reviews,}
    return render(request, 'book_reviews/my_read_list.html', context)


@login_required
def add_review_view(request, read_book_id):
    """Adding a users review to a read book"""
    book_read = ReadBook.objects.get(id=read_book_id)

    if request.user != book_read.reader:
        raise Http404

    if request.method != 'POST':
        form = BookReviewForm
    else:
        form = BookReviewForm(data=request.POST)
        if form.is_valid():

            review = form.save(commit=False)
            review.read = book_read
            review.title = book_read.book_title
            review.user = book_read.reader
            review.save()
            return redirect('book_reviews:my_read_list')

    context = {'form': form, 'read_book_id': read_book_id,}
    return render(request, 'book_reviews/add_review.html', context)


@login_required
def edit_review_view(request, book_review_id):
    """Editing an existing review by the user"""
    review = BookReview.objects.get(id=book_review_id)
    if review.user != request.user:
        raise Http404

    if request.method != 'POST':
        form = BookReviewForm(instance=review)
    else:
        form = BookReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book_reviews:my_read_list')

    context = {'review': review, 'form': form,}
    return render(request, 'book_reviews/edit_review.html', context)

