from django.shortcuts import render, redirect
from django import  views
from .models import UserMOdel

# Create your views here.

class GetUsersView(views.View):
    def get(self, request):
       allUser = UserMOdel.objects.all() 
       template_name ='main/list.html'
       context = {
           'users': allUser
           }
       return render(request, template_name, context)