from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/index.html', context={ 
        'recipes': recipes,

    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={ 
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
