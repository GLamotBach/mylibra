from public_profile.models import UsersPublicProfile

def navbar_data_renderer(request):
    logged_user = UsersPublicProfile.objects.get(user_id=request.user)
    return {'logged_user': logged_user,}

