from django.shortcuts import render
from .models import Task
from .forms import AddTaskForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    context = {
        'tasks': Task.objects.filter(author=request.user),
    }

    return render(request, 'to_do/home.html', context)


@login_required(login_url='login')
def addTask(request):
    form = AddTaskForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        form = AddTaskForm()

    context = {
        'form': form,

    }

    return render(request, 'to_do/home.html', context)
