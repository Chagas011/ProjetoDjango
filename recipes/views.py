
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.db.models import Q
from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(
        is_publish=True
    ).order_by('-id')

    return render(request, 'recipes/pages/index.html',  context={'recipes': recipes})  # noqa: E501


def category(request, category_id):

    recipes = get_list_or_404(Recipe, category__id=category_id, is_publish=True)  # noqa: E501

    return render(request, 'recipes/pages/category.html', context={  # noqa: 501, E261
        'recipes': recipes,
        'tittle': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_publish=True)

    return render(request, 'recipes/pages/recipe.html', context={  # noqa: 501, E261
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(  # noqa: 501, E261
        Q( # noqa: 501, E261
            Q(title__icontains=search_term) | # noqa: 501, E261
            Q(description__icontains=search_term),
        ),
        is_publish=True
        ).order_by('-id')


    return render(request, 'recipes/pages/search.html', context={  # noqa: 501, E261
        'page_title': f'{search_term} |',
        'search_term': search_term,
        'recipes': recipes,
    })
