from django.db import models
from authentication.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    User = models.ForeignKey(User, related_name='movies', on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering = ['-created_at']


