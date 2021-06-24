from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm

# Create your views here.
def shop_index(request):
    
    return render(request, 'shop_index.html')