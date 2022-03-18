from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe
# Create your views here.


def home(request):
    recipes = get_list_or_404(Recipe.objects.filter(
        is_publish=True
    ).order_by('-id'))

    return render(request, 'recipes/pages/index.html',  context={'recipes': recipes})  # noqa: E501


def category(request, category_id):

    recipes = get_list_or_404(Recipe, category__id=category_id, is_publish=True)  # noqa: E501

    return render(request, 'recipes/pages/category.html', context={ # noqa: 501, E261
        'recipes': recipes,
        'tittle': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_publish=True)

    return render(request, 'recipes/pages/recipe.html', context={  # noqa: 501, E261
        'recipe': recipe,
        'is_detail_page': True,
    })
