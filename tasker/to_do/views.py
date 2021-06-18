from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Task
from users.models import Profile
from .forms import AddTaskForm, OrderTasks
from .filters import TaskFilter


@login_required(login_url='login')
def home(request):
    sort_form = OrderTasks()

    """
    Defaultly, the tasks are being sorted by newest descendingly and pushing 
    finished tasks to the bottom of the stack
    """

    tasks = Task.objects.filter(
        author=request.user).order_by('finished', '-id')

    if request.method == 'POST':
        sort_form = OrderTasks(request.POST)

        try:
            sort_form_value = sort_form['method'].value()
        except KeyError as e:
            pass

        if sort_form_value == 'priority':
            tasks = Task.objects.filter(
                author=request.user).order_by('finished', '-priority')

        elif sort_form_value == 'deadline':
            tasks = Task.objects.filter(
                author=request.user).order_by('finished', 'deadline')

    else:  # if request.method == 'GET'
        tasks = Task.objects.filter(
            author=request.user).order_by('finished', '-id')

    context = {
        'tasks': tasks,
        # number of incompleted tasks
        'incomplete': Task.objects.filter(author=request.user, finished=False).count(),
        'form': sort_form
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
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # copy data from post request
        data = request.POST.copy()

        if request.POST.get('finished'):
            data.update({
                "author": request.user,
            })
            profile.total_tasks_finished += 1
        else:
            data.update({
                "author": request.user,
                "updated": True,
            })

        form = AddTaskForm(data, instance=task)

        if form.is_valid():
            profile.save()
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
