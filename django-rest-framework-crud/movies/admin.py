from django.contrib import admin
from .models import Movie
from authentication.models import User
admin.site.register(Movie)
admin.site.register(User)
