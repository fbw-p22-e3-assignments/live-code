from django.urls import path
from . import views
from .views import ContactFormView

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<slug:slug>/", views.post_detail, name="post-detail"),
    path("contact/", ContactFormView.as_view(), name="contact"),
]