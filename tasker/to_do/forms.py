from .models import Task
from django import forms


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'author',
                  'finished', 'updated', 'priority']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'cols': 40
            })
        }


class OrderTasks(forms.Form):
    METHOD_CHOICE = [
        ('newest', 'Newest'),
        ('deadline', 'Deadline'),
        ('priority', 'Priority'),
    ]

    method = forms.CharField(
        label="", widget=forms.Select(choices=METHOD_CHOICE))
