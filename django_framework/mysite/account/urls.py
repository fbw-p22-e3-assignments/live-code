from django.urls import path
from . import views
# Import built in django authentication views
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    # path("login/", views.user_login, name="login"),
    # Create paths to utilize built in views
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),   
]
