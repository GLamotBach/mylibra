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
def lend_accept_view(request, lend_request_id):
    """View for handling accepting a lend_request"""
    lend_request = LendRequest.objects.get(id=lend_request_id)

    lend_accept = LendCopy.objects.get_or_create(
        from_user=lend_request.copy_owner,
        to_user=lend_request.requesting_user,
        copy=lend_request.copy
    )
    # Usunięcie requesta ?
    return redirect('lend_manager:lend_overview')


@login_required
def lend_overview_view(request):
    """Summary overview of all book lent to and from the user"""
    lend_requests_by_user = LendRequest.objects.filter(requesting_user=request.user).select_related()
    lend_requests_to_user = LendRequest.objects.filter(copy_owner=request.user).select_related()

    context = {'lend_requests_by_user': lend_requests_by_user, 'lend_requests_to_user': lend_requests_to_user}
    return render(request, 'lend_manager/lend_overview.html', context)




