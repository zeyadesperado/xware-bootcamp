from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from useraccount.forms import LoginForm, SignupForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def logout_page(request):
    logout(request)
    return redirect(reverse('login'))


def home(request):
    return render(request, 'blog/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            return redirect('login')
        else:
            return render(request, 'register/signup.html', {
                'result': 'Not Valid Data',
                'errors': str(form.errors),
            })

    return render(request, 'register/signup.html', {
        'model_name': 'Signup',
        'result': '',
    })

def login_page(request):
    template_data = {
        'result': '',
    }

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                template_data['result'] = 'Logged In'
                return redirect('home')
            else:
                template_data['result'] = 'wrong data'
        else:
            return render(request, 'login/login.html', {
                'result': 'Not Valid Data',
                'errors': str(form.errors),
            })

    return render(request, 'login/login.html', template_data)