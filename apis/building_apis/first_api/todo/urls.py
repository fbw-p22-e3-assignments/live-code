from .views  import TodoListApiView
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('', TodoListApiView.as_view(), name='todo-list'),
]
