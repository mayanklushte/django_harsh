from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm


# Create your views here.
def shop_index(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.error)
    else:
        form = DemoForm()
    return render(request, 'shop_index.html', {'form': form})