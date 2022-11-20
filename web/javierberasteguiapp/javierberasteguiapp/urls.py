from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/python', include('python.urls')),
    path('backend/', include('backend.urls')),
    path('ciencia-de-datos/', include('datos.urls')),
    path('', include('python.urls'))
]
