from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .models import BookCopy, BookTitle
from .forms import BookTitleForm, BooKCopyForm


def index(request):
    """Main page"""
    return render(request, 'personal_collection/index.html')


@login_required
def myshelf_view(request):
    """Page containing user's book collection"""
    books = BookCopy.objects.filter(owner=request.user).order_by('add_date')

    context = {'books': books}
    return render(request, 'personal_collection/myshelf.html', context)


@login_required
def copy_view(request, copy_id):
    """Detailed information about a book copy"""
    copy = BookCopy.objects.get(id=copy_id)
    title = BookTitle.objects.get(id=copy.book_title_id)

    if copy.owner != request.user:
        raise Http404

    context = {'copy': copy, 'title': title}
    return render(request, 'personal_collection/copy.html', context)


@login_required
def new_title_view(request):
    """Adding a new title"""
    if request.method != 'POST':
        form = BookTitleForm()
    else:
        form = BookTitleForm(data=request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.added_by = request.user
            title.save()
            return redirect('personal_collection:add_to_collection', title_id=title.id)

    context = {'form': form}
    return render(request, 'personal_collection/new_title.html', context)


@login_required
def add_to_collection_view(request, title_id):
    """Adding a book copy to a user's collection"""
    title = BookTitle.objects.get(id=title_id)

    if title.added_by != request.user:
        raise Http404

    if request.method != 'POST':
        form = BooKCopyForm()
    else:
        form = BooKCopyForm(data=request.POST)
        if form.is_valid():
            add_book = form.save(commit=False)
            add_book.owner = request.user
            add_book.book_title = title
            add_book.save()
            return redirect('personal_collection:myshelf')

    context = {'title': title, 'form': form }
    return render(request, 'personal_collection/add_to_collection.html', context)


@login_required
def edit_title_view(request, copy_id):
    """Editing a book title"""
    copy = BookCopy.objects.get(id=copy_id)
    book = BookTitle.objects.get(id=copy.book_title_id)

    if copy.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BookTitleForm(instance=book)
    else:
        form = BookTitleForm(request.POST, request.FILES, instance=book,)
        if form.is_valid():
            form.save()
            return redirect('personal_collection:copy', copy_id=copy_id)

    context = {'copy': copy, 'book': book, 'form': form,}
    return render(request, 'personal_collection/edit_title.html', context)