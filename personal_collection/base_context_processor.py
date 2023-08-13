from public_profile.models import UsersPublicProfile

def navbar_data_renderer(request):
    """Context for navbar."""
    if request.user.is_authenticated:
        logged_user = UsersPublicProfile.objects.filter(user_id=request.user).first()

        return {'logged_user': logged_user,}

    else:
        return {}

