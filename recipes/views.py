from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination
from .models import Recipe
import os
# Create your views here.

PER_PAGE = os.environ.get('PER_PAGE', 4)


def home(request):
    recipes = Recipe.objects.filter(
        is_publish=True
    ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/index.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range
        })  # noqa: E501


def category(request, category_id):
    recipes = get_list_or_404(Recipe, category__id=category_id, is_publish=True)  # noqa: E501
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/category.html', context={  # noqa: 501, E261
        'recipes': page_obj,
        'pagination_range': pagination_range,
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
        Q(  # noqa: 501, E261
            Q(title__icontains=search_term) |  # noqa: 501, E261
            Q(description__icontains=search_term),
        ),
        is_publish=True
        ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', context={  # noqa: 501, E261
        'page_title': f'{search_term} |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'addtional_url': f'&search={search_term}'

    })
