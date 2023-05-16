from rest_framework import serializers
from .models import Todo
from django import forms

class TodoSerializer(serializers.ModelSerializer):
    """Processes the model into JSON using the defined fields"""
    class Meta:
        model = Todo
        fields = ['task', 'details', 'completed']
        
# class TodoForm(forms.ModelForms):
#     class Meta:
#         model = Todo
#         fields = ['task', 'details', 'completed']
    
    
        