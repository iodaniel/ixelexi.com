# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html',{

#     })
from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
]