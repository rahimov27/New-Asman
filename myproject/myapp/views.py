from ast import Return
from os import name
from django.shortcuts import redirect, render
from .models import *
from .forms import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        forms = ClientForm()
    return render(request, 'contact.html', {'form': forms})
