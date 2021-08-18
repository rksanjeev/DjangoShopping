from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.

def register_account(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.email = registration_form.cleaned_data['email']
            user.set_password(registration_form.cleaned_data['password'])
            user.is_active = False
            user.save()

