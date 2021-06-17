from .models import Task
from django import forms


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'author',
                  'finished', 'updated', 'priority', 'deadline']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'cols': 40
            }),
            'priority': forms.Select(attrs={'class': 'drop-down'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'drop-down'}, )
        }


class OrderTasks(forms.Form):
    METHOD_CHOICE = [
        ('newest', 'Newest'),
        ('deadline', 'Deadline'),
        ('priority', 'Priority'),
    ]

    method = forms.CharField(
        label="", widget=forms.Select(attrs={'class': 'drop-down'}, choices=METHOD_CHOICE))
