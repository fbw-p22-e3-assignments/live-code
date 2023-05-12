from .views  import TodoListApiView, TodoDetailApiView
from django.urls import path

app_name = 'todo'

urlpatterns = [
    path('', TodoListApiView.as_view(), name='todo-list'),
    path('<int:todo_id>/', TodoDetailApiView.as_view(), name='todo-detail'),
]
