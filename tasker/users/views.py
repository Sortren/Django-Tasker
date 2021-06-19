from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # getting an user's instance from a form
            user = form.save(commit=False)
            profile = Profile(user=user)  # assigning the user to profile table
            user.save()
            profile.save()

            return redirect('to_do-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile
    }

    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def reset_stats(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        profile.total_tasks_finished = 0
        profile.save()

    return redirect('profile')
