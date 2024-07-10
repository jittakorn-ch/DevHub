from django.urls import path
from main.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register', register, name='register'),
    path('login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('dashboard', dashboard, name='dashboard'),
]