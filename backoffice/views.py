from django.shortcuts import render
from random import randint


def login(request):
    return render(request, 'backoffice/login.html', {})

