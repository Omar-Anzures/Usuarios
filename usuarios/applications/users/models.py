from django.db import models

from .managers import UserManager

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin    


class User(AbstractBaseUser,PermissionsMixin):
    GENER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros')
    )
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    genero = models.CharField(max_length=1,choices=GENER_CHOICES,blank=True)
    
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['email',]

    USERNAME_FIELD = 'username'

    def get_short_name(self,):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

