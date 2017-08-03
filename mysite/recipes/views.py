from django.shortcuts import render
from mysite.recipes.models import Recipe


def recipes(request):
    entries = Recipe.objects.all().order_by('title')

    return render(request, 'recipes/recipes.html', {'recipes': entries})


def recipe(request, input_id):
    entry = Recipe.objects.get(pk=input_id)
    return render(request, 'recipes/recipe.html', {'recipe': entry})

