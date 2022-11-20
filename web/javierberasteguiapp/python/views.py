from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    return HttpResponse("Hello world")

def home(request):
    template_home = open("/home/alter_ego91/Proyectos/web/javierberasteguiapp/python/template/python/index.html")
    template = Template(template_home.read())
    template_home.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)
