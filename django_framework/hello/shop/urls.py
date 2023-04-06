from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.listing, name='browse'),
    path('<int:item_id>/', views.item), 
]
