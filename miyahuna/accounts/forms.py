from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class loginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))
