from django.urls import path

from . import views

app_name = "page"
urlpatterns = [
    path("", views.index, name="index"),
    path("python/", views.python, name="python"),
]