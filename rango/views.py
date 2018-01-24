from django.shortcuts import render
from django.http import HttpResponse

#Creating a view index
def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

#Creating a view about
def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")