from django.contrib import admin
from django.urls import path
from .views import helloworld,hellostudent, increment, reset, decrement
urlpatterns = [
    path('helloworld/', helloworld),
    path('hellostudents/', hellostudent),
    path('decrement/', decrement),
    path('reset/', reset),
    path('increment/', increment),
]
