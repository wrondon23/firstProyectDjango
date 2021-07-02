from django.urls import reverse
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

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Profile(models.Model):

    user_id = models.OneToOneField(UserMOdel, on_delete= models.CASCADE)
    profile_image = models.ImageField(upload_to ='users/profiles/photos', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_id.full_name

    @property
    def get_image_url(self):
        return self.profile_image.url

