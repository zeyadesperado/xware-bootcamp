from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'timestamp', 'author')  # Include 'timestamp' here

admin.site.register(Blog, BlogAdmin)
