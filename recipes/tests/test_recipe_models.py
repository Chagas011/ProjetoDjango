
from django.core.exceptions import ValidationError
from parameterized import parameterized
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

    @parameterized.expand([ # noqa 501
            ('title', 65), # noqa 501
            ('description', 165),  # noqa 501
            ('preparation_time_unit', 65),  # noqa 501
            ('servings_unit', 65)

        ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
