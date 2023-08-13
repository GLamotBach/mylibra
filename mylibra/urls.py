from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from personal_collection import views
from public_profile import views
from friend_list import views
from book_reviews import views
from lend_manager import views

urlpatterns = [
    # Admin functions.
    path('admin/', admin.site.urls),
    # User account handling.
    path('users/', include('users.urls')),
    # Book collections.
    path('', include('personal_collection.urls')),
    # Public profiles of users.
    path('profile/', include('public_profile.urls')),
    # Friend list functionality.
    path('friend/', include('friend_list.urls')),
    # Book reviews and ratings.
    path('review/', include('book_reviews.urls')),
    # Book lending manager.
    path('lend/', include('lend_manager.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)