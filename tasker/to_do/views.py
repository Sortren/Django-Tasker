from django.shortcuts import render
from .models import Task


def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'to_do/home.html', context)
