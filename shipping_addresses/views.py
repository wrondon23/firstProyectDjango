from django import views
from shipping_addresses.models import ShippingAddress
from .forms import shippingAddressForm
from main.models import UserMOdel

from django.shortcuts import redirect, render


#Mostrando el detalle de las direcciones en los usuarios
def GetaddressesView(request, id):
    address = ShippingAddress.objects.get(pk =id)
    template_name ='shipping_addresses/detail.html'
    context = {
        'address': address,
        }
    return render(request,template_name,context)

#creacion de una nueva direccion para los usuarios
class CreateShippingAddressViews(views.View):
    action ='create'
    temple_name = 'shipping_addresses/form.html'
 
 #metodo get para mostrar los campos del formulario
    def get(self, request, user_id):
        address_form = shippingAddressForm()
        user =  UserMOdel.objects.get(pk = user_id)
        context ={
           'form':address_form,
           'action': self.action,
           'user' : user
        }

        return render(request, self.temple_name, context)

    def post(self, request , user_id):
        new_address = shippingAddressForm(request.POST)
        user = UserMOdel.objects.get(pk = user_id)

        if new_address.is_valid():
            new_address_data = new_address.save(commit=False)
            new_address_data.user_id = user
            new_address_data.save()

            return redirect('addresses:detail' , new_address_data.id)
        else:
            context ={
           'form':new_address,
           'action': self.action,
           'user' : user
        }
            return render(request, self.temple_name, context)

class UpdateShippingAddressViews(views.View):
    action ='update'
    temple_name = 'shipping_addresses/form.html'

    def get(self, request, id):
        address = ShippingAddress.objects.get(pk =id)
        adress_form = shippingAddressForm(instance=address)
        context ={
           'form':adress_form,
           'action': self.action,
           'user' : address.user_id,
           'address':address
        }

        return render(request, self.temple_name, context)

    def post(self, request ,id):
        address = ShippingAddress.objects.get(pk =id)
        update_address_form = shippingAddressForm(request.POST, instance=address)

        if update_address_form.is_valid():
            update_address_form.save()
            return redirect('addresses:detail' , id)
        else:
            adress_form = shippingAddressForm(request.POST, instance=address)
            context ={
                'form':adress_form,
                'action': self.action,
                'user' : address.user_id,
                'address':address
                }
            return render(request, self.temple_name, context)

def DeleteShippinAddressView(request,id):
    address = ShippingAddress.objects.get(pk = id)
    user = address.user_id
    address.delete()
    return redirect('user:detail' , user.id)

