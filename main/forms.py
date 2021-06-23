from django import forms
from .models import UserMOdel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserMOdel
        fields ='__all__'