from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)  # Optional: comma-separated tags

    def __str__(self):
        # Reason: Useful for admin display and debugging
        return f"{self.title} by {self.user.username}"
