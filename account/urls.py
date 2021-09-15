from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views
from .forms import UserLoginForm, UserPasswordResetForm, UserPasswordConfirmForm

app_name = 'account'

urlpatterns = [
    # Registration and dashboard
    path('register/', views.register_account, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_account, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Login/logout
    path('login/',
         auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    # Profile Edit/Delete
    path('profile/edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/delete-profile/', views.delete_profile, name='delete_profile'),
    # Reset password
    path('password-reset/', auth_views.PasswordResetView.as_view(
                                                        template_name='account/user/password_reset_form.html',
                                                        success_url='password_reset_done',
                                                        email_template_name='account/user/password_reset_email.html',
                                                        form_class=UserPasswordResetForm),
                                                        name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                                                        template_name='account/user/password_reset_confirm.html',
                                                        success_url='password_reset_complete',
                                                        form_class =UserPasswordConfirmForm
                                                        ), name='password_reset_confirm'),
    path('password-reset/password-reset-email-confirm/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_done'),
    path('password-reset-confirm/Mg/password-reset-complete/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password_reset_complete'),


]
