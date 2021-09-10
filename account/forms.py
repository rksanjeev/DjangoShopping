from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label="User Name",
        min_length=4,
        max_length=50,
        help_text="Required"
    )
    email = forms.EmailField(
        label='Email',
        help_text="Required",
        error_messages={'required': 'Sorry, you will need an email'}
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_user_name(self):
        username = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=username)
        if r.count():
            return forms.ValidationError("User already exists!")
        return username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        {'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-user'}))
    password = forms.CharField(widget=forms.PasswordInput(
        {'class': 'form-control mb-3', 'placeholder': 'Password', 'id':'login-pwd'}))