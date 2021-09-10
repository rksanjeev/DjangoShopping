from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', views.register_account, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_account, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),


    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name='login')
]