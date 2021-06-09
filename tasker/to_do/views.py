from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    context = {
        'tasks': Task.objects.filter(author=request.user)
    }
    return render(request, 'to_do/home.html', context)
