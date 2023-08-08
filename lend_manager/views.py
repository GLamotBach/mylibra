from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from personal_collection. models import BookCopy
from .models import LendRequest, LendCopy

@login_required
def lend_request_view(request, copy_id):
    """View for handling lend request forms"""
    book_copy = BookCopy.objects.get(id=copy_id)
    requesting_user = request.user
    copy_owner = book_copy.owner

    lend_request = LendRequest.objects.get_or_create(
        requesting_user=requesting_user,
        copy_owner=copy_owner,
        copy=book_copy)

    return redirect('lend_manager:lend_overview')


@login_required
def cancel_lend_request_view(request, lend_request_id):
    """View for handling cancellation of a request"""
    canceled_request = LendRequest.objects.get(id=lend_request_id)
    if request.user != canceled_request.requesting_user:
        raise Http404
    else:
        canceled_request.delete()

    return redirect('lend_manager:lend_overview')


@login_required
def refuse_lend_request_view(request, lend_request_id):
    """View for handling refusing a lend request"""
    refused_request = LendRequest.objects.get(id=lend_request_id)
    if request.user != refused_request.copy_owner:
        raise Http404
    else:
        refused_request.delete()

    return redirect('lend_manager:lend_overview')


@login_required
def lend_accept_view(request, lend_request_id):
    """View for handling accepting a lend_request"""
    lend_request = LendRequest.objects.get(id=lend_request_id)

    lend_accept = LendCopy.objects.get_or_create(
        from_user=lend_request.copy_owner,
        to_user=lend_request.requesting_user,
        copy=lend_request.copy
    )
    lend_request = LendRequest.objects.get(id=lend_request_id).delete()
    return redirect('lend_manager:lend_overview')


@login_required
def book_return_confirmation_view(request, lend_copy_id):
    """Page for confirming a book return"""
    return_book = LendCopy.objects.filter(id=lend_copy_id).select_related().first()

    context = {'return_book': return_book, 'lend_copy_id': lend_copy_id}
    return render(request, 'lend_manager/return_confirmation.html', context)


@login_required
def book_return_view(request, lend_copy_id):
    """View for handling returning of a book"""
    returned_book = LendCopy.objects.get(id=lend_copy_id)
    if returned_book.from_user != request.user:
        raise Http404
    else:
        returned_book = LendCopy.objects.get(id=lend_copy_id).delete()
        return redirect('lend_manager:lend_overview')


@login_required
def lend_overview_view(request):
    """Summary overview of all book lent to and from the user"""
    lend_requests_by_user = LendRequest.objects.filter(requesting_user=request.user).select_related()
    lend_requests_to_user = LendRequest.objects.filter(copy_owner=request.user).select_related()
    books_lend_by_user =  LendCopy.objects.filter(from_user=request.user).select_related()
    books_lend_to_user = LendCopy.objects.filter(to_user=request.user).select_related()

    context = {
        'lend_requests_by_user': lend_requests_by_user,
        'lend_requests_to_user': lend_requests_to_user,
        'books_lend_by_user': books_lend_by_user,
        'books_lend_to_user': books_lend_to_user,
    }
    return render(request, 'lend_manager/lend_overview.html', context)






