from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "ams"
urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True)),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('reset-password/',auth_views.PasswordChangeView.as_view(template_name='reset-password.html', success_url='/ams/reset-password-done'), name='reset-password'),
    path('reset-password-done/',auth_views.PasswordChangeDoneView.as_view(template_name='reset-password-done.html',extra_context={'msg':'Reset Password Successful'}), name='reset-password-done'),
    path('register/',views.register, name='register'),
]