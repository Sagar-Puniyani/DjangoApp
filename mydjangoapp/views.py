from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'home.html')


def about(request):
    return HttpResponse("Hello Duniya ! you are on Django About page")


def contact(request):
    return HttpResponse("Hello Duniya ! you are on Django Contact page")

def temp(request):
    return render(request , 'web/index.html')