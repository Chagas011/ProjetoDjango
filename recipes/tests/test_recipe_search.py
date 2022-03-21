from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeSearchTest(TestCase):
    def test_recipe_search_url(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

    def test_recipe_search_view(self):
        viewc = resolve(reverse('recipes:search'))
        self.assertIs(viewc.func, views.search)

    def test_recipe_search_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
