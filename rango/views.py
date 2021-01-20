from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Here you'll find the <a href='/rango/about/'>About</a> page.")

def about(request):
    return HttpResponse("Rango says here is the about page. Here you'll find the <a href='/rango/'>Index</a> page.")



