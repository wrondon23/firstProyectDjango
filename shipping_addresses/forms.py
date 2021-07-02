from .models import ShippingAddress
from django import forms

class shippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude =  ['user_id']