from django.contrib import admin
from .models import Profile, UserMOdel

# Register your models here.
admin.site.register(UserMOdel)
admin.site.register(Profile)

