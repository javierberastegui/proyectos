from django.urls import path

from . import views

urlpatterns = [
    path("python/", views.index, name="index"),
    path("", views.home, name="home")
]