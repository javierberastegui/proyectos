from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "page/index.html")


def python(request):
    return render(request, "page/python.html")


def contact(request):
    return render(request, "page/contact.html")


# def backend(request):
#     return HttpResponse("Esta es la vista backend")

# def contacto(request):
#     return HttpResponse("Esta es la vista contacto")