from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    prepopulated_fields = {"slug":('title',)}
