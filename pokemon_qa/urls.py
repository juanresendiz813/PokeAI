from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon/', include('pokemon.urls')),
    path('', include('pokemon.urls')),
]
