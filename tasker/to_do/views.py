from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# tasks = [
#     {
#         'user': 'Maks',
#         'title': 'Bicycle',
#         'content': 'Replace wheels in the bicycle',
#         'date_posted': 'June 2, 2021'

#     },
#     {
#         'user': 'Maks',
#         'title': 'Recylce Bin',
#         'content': 'Throw thrash to the recycle bin',
#         'date_posted': 'June 4, 2021'
#     },
#     {
#         'user': 'Maks',
#         'title': 'Bicycle',
#         'content': 'Replace wheels in the bicycle',
#         'date_posted': 'June 2, 2021'

#     },
#     {
#         'user': 'Maks',
#         'title': 'Recylce Bin',
#         'content': 'Throw thrash to the recycle bin',
#         'date_posted': 'June 4, 2021'
#     },
#     {
#         'user': 'Maks',
#         'title': 'Bicycle',
#         'content': 'Replace wheels in the bicycle',
#         'date_posted': 'June 2, 2021'

#     },
#     {
#         'user': 'Maks',
#         'title': 'Recylce Bin',
#         'content': 'Throw thrash to the recycle bin',
#         'date_posted': 'June 4, 2021'
#     }
# ]


def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'to_do/home.html', context)
