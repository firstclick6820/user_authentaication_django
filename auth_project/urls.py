
from django.contrib import admin
from django.urls import path, include 
import django.contrib.auth.urls 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users_app.urls')),
    path('user/', include(django.contrib.auth.urls)),
    path('user/', include('users_app.urls')),
    
    
]
