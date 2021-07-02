
from shipping_addresses.models import ShippingAddress
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect
from django import  views
from django.views.generic.base import TemplateView
from .models import UserMOdel
from .forms import Profile_form, UserForm
from django.contrib import messages
from .forms import Profile

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
        'user': user,

        }
    return render(request,template_name,context)


#Crear nuevo usuario
class createUserView(views.View):
    action = 'create'
    template_name = 'main/form.html'

    #metodo get para mostrar los campos del formularios de usuarios
    def get(self, request):
        user_form = UserForm()
        profile_form = Profile_form()
        context = {
            'user_form': user_form,
            'profile_form' : profile_form,
            'action': self.action
        }
        return render(request, self.template_name, context)
    #Metodos post para envios de los datos del formulario de usuario
    def post(self, request):
        new_user_form = UserForm(request.POST)
        new_profile_form = Profile_form(request.POST, request.FILES)

        if new_user_form.is_valid() and new_profile_form.is_valid():
            new_user_data = new_user_form.save()
            new_profile_data = new_profile_form.save(commit = False)
            new_profile_data.user_id = new_user_data
            new_profile_data.save()
            messages.success(request,'Usuario creado exitosamente!')
            return redirect('user:list')
        else:
            errors = new_user_form.errors.as_data()
            print(errors)
            user_form = UserForm()
            profile_form = Profile_form()
            context = {
            'user_form': user_form,
            'profile_form' : profile_form,
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

        user_form = UserForm(instance = user )
        profile_form = Profile_form(instance= user.profile)
        context = {
        'user': user,
        'action': self.action,
        'user_form': user_form,
        'profile_form' : profile_form
          }

        return render(request, self.template_name, context)

    def post(self, request, id):
        user = UserMOdel.objects.get(id=id)

        edit_user_form = UserForm(request.POST, instance=user)
        edit_profile_form = Profile_form(request.POST, request.FILES, instance=user.profile,)

        if edit_user_form.is_valid() and edit_profile_form.is_valid():
            edit_user_data = edit_user_form.save()
            edit_profile_data = edit_profile_form.save(commit = False)
            edit_profile_data.user = edit_user_data
            edit_profile_data.save()
            messages.success(request, 'Usuario Actualizado exitosamente')
            return redirect('user:detail', id)
        else:

            errors = edit_user_form.errors.as_data()
            print(errors)
            user_form = UserForm(instance = user )
            profile_form = Profile_form(instance= user.profile)
            context = {
                'user': user,
                'action': self.action,
                'user_form': user_form,
                'profile_form' : profile_form
          }
            messages.error(request, 'ERROR:Algo fallo al editar la informacion del usuario')

            return render(request, self.template_name, context)

def DeleteUserView(request,id):
    user = UserMOdel.objects.get(id = id)
    user.delete()
    messages.success(request, 'Usuario eliminado')

    return redirect('user:list')


