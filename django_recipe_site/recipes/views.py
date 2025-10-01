from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Recipe
from .forms import RecipeForm
from .ai import generate_recipe_from_ingredients

@login_required(login_url='/users/login/')
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'recipes/list.html', {'recipes': recipes})

@login_required(login_url='/users/login/')
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

@login_required(login_url='/users/login/')
def generate_recipe(request):
    generated_recipe = None
    if request.method == 'POST' and 'save' not in request.POST:
        ingredients = request.POST.get('ingredients', '')
        if ingredients:
            generated_recipe = generate_recipe_from_ingredients(ingredients)
            ingredients = generated_recipe['ingredients']
    elif request.method == 'POST' and 'save' in request.POST:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes:detail', pk=recipe.pk)
    return render(request, 'recipes/generate.html', {'generated_recipe': generated_recipe})

@login_required(login_url='/users/login/')
def manual_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes:detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/manual.html', {'form': form})

@login_required(login_url='/users/login/')
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit.html', {'form': form, 'recipe': recipe})

@login_required(login_url='/users/login/')
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:list')
    return render(request, 'recipes/delete.html', {'recipe': recipe})
