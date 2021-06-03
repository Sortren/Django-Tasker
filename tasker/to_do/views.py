from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'to_do/home.html')


def login(request):
    return render(request, 'to_do/login.html')


def register(request):
    return render(request, 'to_do/register.html')
