from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome),
    path('Reg',views.Reg),
    path('Login',views.Login),
    path('details',views.details),
    path('delete',views.delete),
    path('assignment',views.assignment),
]    