from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


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
