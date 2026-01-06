from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = ['1.gif', '2.gif', '3.gif', '4.gif']
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    return render(request, 'contact.html')
