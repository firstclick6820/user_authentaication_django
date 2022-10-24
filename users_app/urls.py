from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login', views.user_login, name='user_login'),
    path('register', views.user_regiser, name='user_register'),
    path('logout', views.user_logout, name='user_logout')
]
