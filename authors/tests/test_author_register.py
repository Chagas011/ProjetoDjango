from authors.forms import RegisterForm
from django.test import TestCase
from parameterized import parameterized


class AuthorRegisterForm(TestCase):
    @parameterized.expand([
        ('first_name', 'Your first name here'),
        ('last_name', 'Your last name here'),
        ('username', 'Your username here'),
        ('email', 'Your e-mail here'),
        ('password', 'your password here'),
        ('password2', 'Repeat your password here'),
    ])
    def test_placeholder(self, field, placeholder):
        form = RegisterForm()
        placeholders = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, placeholders)

    @parameterized.expand([
        ('email', 'The e-mail must be valid'),
        ('password', 'A senha deve conter mais que 8 chars'),
        ('first_name', 'Your name'),
    ])
    def test_fields_help_text(self, field, placeholder):
        form = RegisterForm()
        placeholders = form[field].field.help_text
        self.assertEqual(placeholder, placeholders)
