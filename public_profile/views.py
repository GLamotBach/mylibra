from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User

from .models import UsersPublicProfile
from .forms import UsersPublicProfileForm
from friend_list.models import FriendList, FriendInvite
from personal_collection.models import BookCopy
from book_reviews.models import ReadBook, BookReview, BookRating


@login_required
def profile_setup_view(request):
    """Initial public profile setup."""

    if request.method != 'POST':
        form = UsersPublicProfileForm()
    else:
        form = UsersPublicProfileForm(request.POST, request.FILES,)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('personal_collection:index')

    context = {'form': form }
    return render(request, 'public_profile/setup.html', context)


@login_required
def edit_profile_view(request):
    """Page for editing user's public profile."""
    profile = UsersPublicProfile.objects.get(user=request.user)

    if profile.user != request.user:
        raise Http404

    if request.method != 'POST':
        form = UsersPublicProfileForm(instance=profile)
    else:
        form = UsersPublicProfileForm(request.POST, request.FILES, instance=profile,)
        if form.is_valid():
            form.save()
            return redirect('personal_collection:index')

    context = {'profile': profile, 'form': form,}
    return render(request, 'public_profile/edit_profile.html', context)


@login_required
def profile_view(request, profile_id):
    """Users public profile page."""
    profile = UsersPublicProfile.objects.get(id=profile_id)

    own_profile = False
    already_friend = False
    invitation_pending = False
    invitation_to_accept = False
    # Check if profile page belongs to the request user.
    if profile.user == request.user:
        own_profile = True
    else:
        # Check if profile page belongs to a friend.
        list_owner = UsersPublicProfile.objects.get(user_id=request.user)
        friends = FriendList.objects.filter(list_owner=list_owner, friend=profile_id)
        if friends.exists():
            already_friend = True
        else:
            # Check if owner of profile page has been invited to friends.
            invitation_send = FriendInvite.objects.filter(from_user=list_owner, to_user=profile_id)
            if invitation_send.exists():
                invitation_pending = True
            else:
                invitation_received = FriendInvite.objects.filter(from_user=profile_id, to_user=list_owner)
                if invitation_received.exists():
                    invitation_to_accept = True

    # Counters for profile statistics.
    count_friends = FriendList.objects.filter(list_owner=profile).count()
    count_collection = BookCopy.objects.filter(owner=profile.user).count()
    count_read = ReadBook.objects.filter(reader=profile.user).count()
    count_reviews = BookReview.objects.filter(user=profile.user).count()
    count_ratings = BookRating.objects.filter(reader=profile.user).count()

    context = {
        'profile': profile,
        'own_profile': own_profile,
        'already_friend': already_friend,
        'invitation_pending': invitation_pending,
        'invitation_to_accept': invitation_to_accept,
        'count_friends': count_friends,
        'count_collection': count_collection,
        'count_read': count_read,
        'count_reviews': count_reviews,
        'count_ratings': count_ratings,

    }
    return render(request, 'public_profile/profile.html', context)


@login_required
def public_book_collection_view(request, profile_id):
    """Public book list of a selected user."""
    profile = UsersPublicProfile.objects.get(id=profile_id)
    book_list = BookCopy.objects.filter(owner=profile.user)

    context = {'profile': profile, 'book_list': book_list}
    return render(request, 'public_profile/public_book_collection.html', context)