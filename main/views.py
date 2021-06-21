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

#buscar un usuario en especifico por id
def DetalleUsuario(request, id):
    user = UserMOdel.objects.get(pk =id)
    template_name ='main/detail.html'
    context = {
        'user': user
        }
    return render(request,template_name,context)

class CreateUserView(views.View):

    template_name = 'main/create.html'
    def get(self,request):
        return render(request,self.template_name)
   
    
