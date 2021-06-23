from django.shortcuts import render, redirect
from django import  views
from django.views.generic.base import TemplateView
from .models import UserMOdel
from .forms import UserForm
from django.contrib import messages

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


#Crear nuevo usuario
class createUserView(views.View):
    action = 'create'
    template_name = 'main/form.html'
    
    def get(self, request):
        form = UserForm()
        context = {
            'form': form,
            'action': self.action
        }
        return render(request, self.template_name, context)

    def post(self, request):
        new_form = UserForm(request.POST)
        if new_form.is_valid():
            form_data = new_form.save(commit=False)
            form_data.save()
            messages.success(request,'Usuario creado exitosamente!')
            return redirect('user:list')
        else:
            errors = new_form.errors.as_data()
            print(errors)
            form = UserForm()
            context = {
            'form': form,
            'action': self.action
            }
            messages.error(request, 'Algo fallo al momento de crear un usuario')
            return render(request, self.template_name, context)

#Actualizar los usuarios
class UpdateUserView(views.View):
    template_name = 'main/form.html'
    action = 'update'

    def get(self, request, id):        
        user = UserMOdel.objects.get(id = id)
        form = UserForm(instance = user)
        context = {
        'user': user,
        'action': self.action,
        'form': form
          }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        user = UserMOdel.objects.get(id=id)
        edit_form = UserForm(request.POST, instance=user)
        if edit_form.is_valid():
            form_data = edit_form.save(commit=False)
            form_data.save()
            messages.success(request, 'Usuario Actualizado exitosamente')
            return redirect('user:detail', id)
        else:
             
            errors = edit_form.errors.as_data()
            print(errors)
            form = UserForm(instance=user)
            context ={
            'form': form,
            'action': self.action,
            'user':user
            }
            messages.error(request, 'ERROR:Algo fallo al editar la informacion del usuario')
            return render(request, self.template_name, context)
            
        
         
def DeleteUserView(request,id):
    user = UserMOdel.objects.get(id = id)
    user.delete()
    messages.success(request, 'Usuario eliminado')
    
    return redirect('user:list')


