from pickle import TRUE
from django.test import TestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.


class RecipeURLsTest(TestCase):
    def test_recipe_home_url(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_recipe_url(self):
        recipe_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(recipe_url, '/recipes/1/')


class RecipeViewsTest(TestCase):
    def test_recipe_home_view(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view(self):
        viewc = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(viewc.func, views.category)

    def test_recipe_recipe_view(self):
        viewr = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(viewr.func, views.recipe)
