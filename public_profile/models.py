from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UsersPublicProfile(models.Model):
    """Publiczny profil dla użytkownika"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public_name = models.CharField(max_length=20)
    location = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    image = models.ImageField(upload_to='images/', null=True,  default='images/placeholder_profile.png')

    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciągu tekstowego"""
        return f"{self.user} - {self.public_name}"
