from django import forms
from django.forms import fields
from .models import Profile, UserMOdel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserMOdel
        fields ='__all__'
        
class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
       # fields =  ['profile_image','bio','is_public']
        exclude =['user_id']
        