# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html',{

#     })
from django.urls import path 

from . import views 

urlpatterns = [
   path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
]
