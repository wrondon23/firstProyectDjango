from django.db import models


GENDER_OPTS =(
    ('male','masculino'),
    ('female','Femenino'),
    ('other','Otros')
)
# Create your models here.

class UserMOdel(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number =models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(choices=GENDER_OPTS, max_length=20)
    date_birth = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f':{self.first_name} {self.last_name}'