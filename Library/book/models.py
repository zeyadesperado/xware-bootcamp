from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    published_year = models.IntegerField()
    published = models.BooleanField(default=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)

class BookDetail(models.Model):
    language = models.CharField(max_length=100)
    page_count = models.IntegerField()
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
class Reader(models.Model):
    name = models.CharField(max_length=120)
    Borrowed_books = models.ManyToManyField(Book)