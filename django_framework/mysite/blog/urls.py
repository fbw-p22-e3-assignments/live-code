from django.urls import path
from . import views
from .views import PostDetail

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<slug:slug>/", PostDetail.as_view(), name="post-detail"),
]