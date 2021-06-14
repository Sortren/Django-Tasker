from .models import Task
from django import forms


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'author', 'finished']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'cols': 40
            })
        }
