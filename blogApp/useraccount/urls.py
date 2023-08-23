from django.urls import path
from useraccount.views import *
urlpatterns = [
    path('register', sign_up, name='register'),
    path('login', login_page, name='login'),
    path('user', login_page, name='user'),
    path('home',home, name='home'),
    path('logout/', logout_page, name='logout')
]