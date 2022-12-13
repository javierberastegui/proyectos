from django.urls import path

from . import views

app_name = "post"
urlpatterns = [
    path("python/hola-mundo-introduccion-a-la-programacion-con-python/", views.post_1, name="post1"),
]