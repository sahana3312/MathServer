
from django.contrib import admin 
from django.urls import path  
from mathapp import views
urlpatterns = [
    path('', views.gst_calculate, name='Total')
]
