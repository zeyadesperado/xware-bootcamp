from django.db import models
from Author.models import Author

class Blog(models.Model):
    title = models.CharField(max_length=130)
    pub_date = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
# Create your models here.
