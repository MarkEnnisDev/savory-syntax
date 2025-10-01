from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('generate/', views.generate_recipe, name='generate'),
    path('manual/', views.manual_recipe, name='manual'),
    path('<int:pk>/', views.recipe_detail, name='detail'),
    path('<int:pk>/edit/', views.edit_recipe, name='edit'),
    path('<int:pk>/delete/', views.delete_recipe, name='delete'),
] 