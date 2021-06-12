from django.shortcuts import render
from .models import Task
from .forms import AddTask
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):

    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(title=data.get('title'), content=data.get(
                'content'), author=request.user)
            task.save()
            form = AddTask()
        else:
            form = AddTask()

    context = {
        'tasks': Task.objects.filter(author=request.user),
        'form': form,
    }

    return render(request, 'to_do/home.html', context)
