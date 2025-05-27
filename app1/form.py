from .models import Task
from django import forms

class TodoList(forms.Form):
    title=forms.CharField(max_length=200)
    desc=forms.Textarea()
    complete=forms.BooleanField()
    