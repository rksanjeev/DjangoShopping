from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
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
        {'class': 'form-control mb-3', 'placeholder': 'Password', 'id': 'login-pwd'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname',
                   'readonly': 'readonly'}))

    full_name = forms.CharField(
        label='Full Name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Name', 'id': 'form-name'}))

    phone_number = forms.CharField(label='Phone Number', min_length=10, max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': '9900990099', 'id': 'form-phone'}))

    address1 = forms.CharField(
        label='Address', min_length=4, max_length=165, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Address Line 1', 'id': 'form-address'})
    )
    postcode = forms.CharField(label='Postal Code', min_length=6, max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': '110001', 'id': 'form-postcode'}))

    address2 = forms.CharField(label='Address Line 2', min_length=0, max_length=165, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Address Line 2', 'id': 'form-address2'}))

    town_city = forms.CharField(label='City', min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'City', 'id': 'form-city'}))

    class Meta:
        model = UserBase
        fields = ('full_name', 'user_name', 'email', 'phone_number', 'address1', 'address2', 'town_city', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = UserBase.objects.filter(email=email)
        if not user:
            raise forms.ValidationError('This email address is invalid!')
        return email


class UserPasswordConfirmForm(SetPasswordForm):
    newpassword1 = forms.CharField(widget=forms.PasswordInput(
        {'class': 'form-control mb-3', 'placeholder': 'Enter New Password', 'id': 'form-new-pwd1'}))
    newpassword2 = forms.CharField(widget=forms.PasswordInput(
        {'class': 'form-control mb-3', 'placeholder': 'Repeat Password', 'id': 'form-new-pwd2'}))