from .models import Task
from django import forms


class AddTaskForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    content = forms.CharField(label='content', widget=forms.Textarea)
