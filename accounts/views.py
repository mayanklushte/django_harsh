from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('wrong credentials')
    else:
        return render(request, 'login.html', {})