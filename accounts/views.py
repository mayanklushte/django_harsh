from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = 'mayank'
    return render(request, 'index.html', {'data': name})


