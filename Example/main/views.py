from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def nav(request):
    return render(request, 'main/nav.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

