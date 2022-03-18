from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class RecipeURLsTest(TestCase):
    def test_recipe_home_url(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')
