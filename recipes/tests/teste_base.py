
from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Categorys'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='outro',
        last_name='name',
        username='outroname',
        password='123456',
        email='outro@email.com'): # noqa: 501, E261

        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        title='Titulo da receita 2',
        description='Receita teste 2',
        slug='titulo-teste-2',
        preparation_time=5,
        preparation_time_unit='minutos',
        servings=5,
        servings_unit='porcoes',
        preparation_steps='como fazer receita teste',
        is_publish=True,
        category_data=None,
        author_data=None,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}
        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            is_publish=is_publish,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )