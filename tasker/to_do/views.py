from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse('<h1>test</h1>')

def login(request):
    return render(request, 'to_do/login.html')

def register(request):
    return render(request, 'to_do/register.html')
