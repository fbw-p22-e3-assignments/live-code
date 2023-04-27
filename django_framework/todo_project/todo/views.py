from django.shortcuts import render, get_object_or_404
from .models import TodoItem


def todo_list(request):
    todo_items = TodoItem.objects.all().order_by('-created_on')
    return render(request, 'index.html', {"todo_items": todo_items})
    
def todo_detail(request, slug, id):
    todo_item = get_object_or_404(TodoItem, id=id, slug=slug)
    return render(request, 'todo_detail.html', {"todo_item": todo_item})
