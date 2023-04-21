from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("<int:task_id>/", views.task_by_id, name="task-by-id"),
]