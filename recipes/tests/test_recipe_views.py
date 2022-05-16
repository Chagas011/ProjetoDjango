from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .teste_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    @skip('in progress')
    def test_recipe_home_template_loads(self):
        self.make_recipe(title='Recipe Title')
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)


class RecipeViews(RecipeTestBase):
    def test_recipe_home_view(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_status(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/index.html')

    def test_recipe_home_ispublish(self):
        self.make_recipe(is_publish=False)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            content
        )

    def test_recipe_category_view(self):
        viewc = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(viewc.func, views.category)

    def test_recipe_category_ispublish(self):
        self.make_recipe(is_publish=False)
        response = self.client.get(
        reverse('recipes:category', kwargs={'category_id': 1}))  # noqa: 501, E261
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipe_view(self):
        viewr = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(viewr.func, views.recipe)

    def test_recipe_recipe_ispublish(self):
        self.make_recipe(is_publish=False)
        response = self.client.get(
        reverse('recipes:recipe', kwargs={'id': 1}))  # noqa: 501, E261
        self.assertEqual(response.status_code, 404)


@skip('faul')
class CategoryViews(RecipeTestBase):
    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)
