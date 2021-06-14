from django.shortcuts import get_object_or_404, redirect, render
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
        data = request.POST.copy()
        data.update({"author": request.user})
        form = AddTaskForm(data)

        if form.is_valid():
            form.save()
            form = AddTaskForm()
        else:
            form = AddTaskForm()
    else:
        form = AddTaskForm()

    context = {
        'form': form,
    }

    return render(request, 'to_do/add_task.html', context)


@login_required(login_url='login')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        # confirm that we want to delete a task
        task.delete()
        return redirect('to_do-home')

    context = {
        "task": task,
    }

    return render(request, 'to_do/delete_task.html', context)


@login_required(login_url='login')
def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.update(title=data.get('title'), content=data.get('content'))
            return redirect('to_do-home')
    else:
        form = AddTaskForm()

    context = {
        "task": task,
        "form": form,
        "name": "update-task",
    }

    return render(request, 'to_do/add_task.html', context)
