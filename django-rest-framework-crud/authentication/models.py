from django.db import models
from django.contrib.auth.models import AbstractUser,User

class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPERUSER = 'superuser', 'SuperUser'
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    role = models.TextField(choices=Roles.choices,null=True,default=Roles.USER)

# Create your models here.
