from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user']  # Add more fields here as the profile expands
        # Reason: Simple ModelForm for user profile management 