from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html', context={'title': 'Первая страница на Django'})

def new(request):
    return render(request, 'main/new.html', context={'title': 'Вторая страница на Django', 'name': 'ДжанГО'})

def nav(request):
    return render(request, 'main/nav.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')