from django.shortcuts import render


def login(request):
    return render(request, 'backoffice/login.html', {})

def home(request):
    return render(request, 'backoffice/home.html', {})
