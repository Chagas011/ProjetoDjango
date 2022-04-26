import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(('Senha fraca'), code='invalid')


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password here'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'your password here'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text='A senha deve conter mais que 8 chars',
        validators=[strong_password]
    )

    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your e-mail here'
        }),
        error_messages={
            'required': 'e-mail must not be empty'
        },
        help_text='The e-mail must be valid'
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username here'
        }), error_messages={
            'required': 'Username must not be empty'
        },
    )

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your first name here'
        }), error_messages={
            'required': 'First name must not be empty'
        },
        help_text='Your name',

    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your last name here'
        }), error_messages={
            'required': 'First name must not be empty'
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',

        ]

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Type your last name here'
            }),
            'password': forms.PasswordInput(attrs={
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError('Email existente', code='invalid')

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
