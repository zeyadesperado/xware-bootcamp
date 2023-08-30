from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from activatable_model.models import BaseActivatableModel


class Blog(models.Model):
    blog_title = models.CharField(max_length=70,default="Untitled")
    blog_text = models.CharField(max_length=500)
    blog_image = models.ImageField(upload_to='',null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Blogger(BaseActivatableModel):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=180)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)