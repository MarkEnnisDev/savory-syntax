from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add additional profile fields here (e.g., bio, avatar) as needed in the future

    def __str__(self):
        # Reason: Provides a readable representation for admin and debugging
        return f"Profile of {self.user.username}"
