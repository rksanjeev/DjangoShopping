from django import forms
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
        error_messages=('This will is required!',)
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