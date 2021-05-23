from django.shortcuts import render
from django.http import HttpResponse
from .models import Journey
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Django'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 + val2
    return render(request, 'result.html', {'result': result})

def index(request):
    jour = Journey()
    jour.home = 'Your Home'
    jour.room = 1
    jour.destination = 'Your Destination'
    #jour.img = 'logo.png'

    jour2 = Journey()
    jour2.home = 'Your Home'
    jour2.room = 1
    jour2.destination = 'Your Destination'
    #jour2.img = 'logo.png'
    
    jours = [jour, jour2]
    return render(request, 'index.html', {'journ': jours})