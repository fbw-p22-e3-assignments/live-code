from .views  import TodoListApiView, TodoDetailApiView
from django.urls import path
# Import method to generate authentication token
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'todo'

urlpatterns = [
    path('', TodoListApiView.as_view(), name='todo-list'),
    path('<int:todo_id>/', TodoDetailApiView.as_view(), name='todo-detail'),
    path('api-auth-token/', obtain_auth_token, name='api-auth-token'),
]
