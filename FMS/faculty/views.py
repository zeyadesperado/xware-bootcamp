from django.shortcuts import render,HttpResponse
from .models import *

def index(request):
    return render(request,'faculty/index.html')


def show(request):
    prof_name = Professor.objects.all()[1]
    # print(Professor.objects.all())
    # print(Professor.objects.filter().first())
    return render(request,'faculty/showdata.html',{'prof_name':prof_name})