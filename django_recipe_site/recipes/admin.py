from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'tags')
    search_fields = ('title', 'ingredients', 'tags')
    list_filter = ('created_at', 'tags')
    # Reason: Improves admin usability for recipe management
