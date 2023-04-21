from django.shortcuts import render
from .models import todos

def task_by_id(request, task_id):
    task = todos[task_id - 1]
    return render(request, 'todo/task-detail.html', {"task_id": task_id, "task":task})
