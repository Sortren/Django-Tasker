from django import forms


class AddTask(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=2000)
