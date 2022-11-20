from django.shortcuts import render
from django.http import HttpResponse

def python(request):
    return HttpResponse("Hola mundo!")