from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task