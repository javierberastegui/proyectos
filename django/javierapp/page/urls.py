from django.urls import path

from . import views

app_name = "page"
urlpatterns = [
    path("", views.index, name="index"),
    path("python/", views.python, name="python"),
    path("contacto/", views.contact, name="contact"),
    path("cv/", views.cv, name="cv")
]