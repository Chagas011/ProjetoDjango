from re import S
from django.core.exceptions import ValidationError
from django.urls import resolve, reverse
from unittest import skip
from recipes import views
from .teste_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_model_title(self):

        self.recipe.title = 'A' * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_model_description(self):

        self.recipe.description = 'A' * 168
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
