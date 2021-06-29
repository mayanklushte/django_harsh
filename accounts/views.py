from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    name = 'mayank'
    return render(request, 'index.html', {'data': name})


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

        else:
            print(form.error)
    else:
        form = UserForm()
    return render(request, 'user_register.html', {'form': form})