from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "python/index.html")

def python(request):
    return HttpResponse("Hola mundo!")