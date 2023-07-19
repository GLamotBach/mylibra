from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from personal_collection. models import BookCopy
from .models import LendRequest

@login_required
def lend_request_view(request, copy_id):
    """View for handling lend request forms"""
    book_copy = BookCopy.objects.get(id=copy_id)
    requesting_user = request.user
    copy_owner = book_copy.owner

    # Check if a request already exists
    lend_request = LendRequest.objects.get_or_create(
        requesting_user=requesting_user,
        copy_owner=copy_owner,
        copy=book_copy)

    return redirect('friend_list:friendlist') # Tymczasowo


@login_required
def lend_overview_view(request):
    """Summary overview of all book lent to and from the user"""
    lend_requests_by_user = LendRequest.objects.filter(requesting_user=request.user).select_related()
    lend_requests_to_user = LendRequest.objects.filter(copy_owner=request.user).select_related()

    context = {'lend_requests_by_user': lend_requests_by_user, 'lend_requests_to_user': lend_requests_to_user}
    return render(request, 'lend_manager/lend_overview.html', context)




