from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def post_1(request):
    return render(request, "post/post-1.html")
