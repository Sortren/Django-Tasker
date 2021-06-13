from django.shortcuts import render
from .models import Task
from .forms import AddTaskForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    context = {
        # Displaying tasks only for logged in user, ordered by id - descendingly (newest task is on top of the stack)
        'tasks': Task.objects.filter(author=request.user).order_by('-id'),
    }

    return render(request, 'to_do/home.html', context)


@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(title=data.get('title'), content=data.get(
                'content'), author=request.user)
            task.save()

            form = AddTaskForm()
    else:
        form = AddTaskForm()

    context = {
        'form': form,
    }

    return render(request, 'to_do/add_task.html', context)
