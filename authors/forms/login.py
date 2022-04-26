
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username here'
        }), error_messages={
            'required': 'Username must not be empty'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password here'
        }), error_messages={
            'required': 'Password must not be empty'
        }
    )
