from django.shortcuts import render
from mysite.recipes.models import Recipe


def recipes(request):
    entries = Recipe.objects.all()

    return render(request, 'recipes/recipes.html', {'recipes': entries})
