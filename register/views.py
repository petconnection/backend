from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from backoffice.forms import EntityForm
from register.models import Token


def register(request, token=None):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix='user_form')
        entity_form = EntityForm(request.POST, prefix='entity_form')
        if user_form.is_valid() and entity_form.is_valid():
            username = user_form.save()
            entity = entity_form.save(commit=False)
            entity.user = User.objects.get(username=username)
            entity.save()
            return redirect('/')
    else:
        token = Token.objects.filter(code=token).first()
        if token and token.is_valid():
            user_form = UserCreationForm(prefix='user_form')
            entity_form = EntityForm(prefix='entity_form')
        else:
            return render(request, 'error.html')

    forms = {'user_form': user_form, 'entity_form': entity_form}
    return render(request, 'index.html', forms)
