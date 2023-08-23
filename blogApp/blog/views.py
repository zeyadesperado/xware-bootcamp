from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogForm 
from django.contrib.auth.decorators import login_required

def myblogs(request: HttpRequest):
    if request.user.is_authenticated:
        user_blogs = Blog.objects.filter(author = request.user)
    else:
        user_blogs = []
        return redirect('blog_home')
    
    return render(request, 'blog/myblogs.html', {'user_blogs': user_blogs})

def blog_home(request: HttpRequest):
    blog_object = Blog.objects.all()
    return render(request,'blog/home.html', {'blog_object':blog_object})


def create_blog(request: HttpRequest):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            print(form.errors)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                blog.save()
                return redirect('blog_home')
        else:
            form = BlogForm()
            # errors: str(form.errors)
            # result = 'is not valid'
        return render(request, 'blog/create_blog.html', {'form': form})
    else:
        return redirect(reverse('login'))
    
    
def edit_blog(request: HttpRequest, blog_id):

    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.blog_title = request.POST['blog_title']
        blog.blog_text = request.POST['blog_text']
        blog.blog_image = request.FILES.get('blog_image')
        blog.save()
        return redirect('blog_home')

    return render(request, 'blog/edit.html', {'blog': blog})


def delete_blog(request: HttpRequest, blog_id):
    
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        blog.delete()
        return redirect('myblogs')
    
    return render(request, 'blog/delete.html', {'blog': blog})