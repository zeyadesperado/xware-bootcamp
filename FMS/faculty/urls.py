from django.urls import path
from faculty.views import *

urlpatterns = [
path('hello/',index),
path('show/',show)
]