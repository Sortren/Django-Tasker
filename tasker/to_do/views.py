from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import AddTaskForm, OrderTasks
from django.contrib.auth.decorators import login_required
from .filters import TaskFilter


@login_required(login_url='login')
def home(request):
    sort_form = OrderTasks()
    tasks = Task.objects.filter(author=request.user).order_by('-id')

    if request.method == 'POST':
        sort_form = OrderTasks(request.POST)
        sort_form_value = sort_form['method'].value()

        if sort_form_value == 'priority':
            tasks = Task.objects.filter(
                author=request.user).order_by('-priority')
        else:
            pass

    else:
        tasks = Task.objects.filter(author=request.user).order_by('-id')

    context = {
        # Displaying tasks only for logged in user, ordered by id - descendingly (newest task is on top of the stack) /by default
        'tasks': tasks,
        'incomplete': Task.objects.filter(author=request.user, finished=False).count(),
        'form': sort_form
    }

    return render(request, 'to_do/home.html', context)

# .order_by('-id')


@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data.update({"author": request.user})
        form = AddTaskForm(data)

        if form.is_valid():
            form.save()
            return redirect('to_do-home')
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
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        # copy data from post request
        data = request.POST.copy()

        if request.POST.get('finished'):
            data.update({
                "author": request.user,
            })
        else:
            data.update({
                "author": request.user,
                "updated": True,
            })

        form = AddTaskForm(data, instance=task)

        if form.is_valid():
            form.save()
            return redirect('to_do-home')
        else:
            form = AddTaskForm(instance=task)
    else:
        form = AddTaskForm(instance=task)

    context = {
        "task": task,
        "form": form,
        "name": "update-task",
    }

    return render(request, 'to_do/add_task.html', context)
