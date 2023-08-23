from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    blog_title = models.CharField(max_length=70,default="Untitled")
    blog_text = models.CharField(max_length=500)
    blog_image = models.ImageField(upload_to='',null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)