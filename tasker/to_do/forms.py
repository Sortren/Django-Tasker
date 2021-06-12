from .models import Task
from django.forms import ModelForm


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']
