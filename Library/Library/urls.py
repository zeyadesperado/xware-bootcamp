"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book.views import *

urlpatterns = [
    path('api/books/', BookApiViews.as_view() ),
    path('api/books/<int:id>', BookApiViews.as_view() ),
    path('visitors/', VisitorList.as_view(), name='visitor-list'),
    path('visitors/<int:pk>/', VisitorRetrive.as_view(), name='visitor-retrieve'),
    path('visitors/create/', VisitorCreation.as_view(), name='visitor-create'),
    path('visitors/update/<int:pk>/', VistorUpdate.as_view(), name='visitor-update'),
    path('visitors/delete/<int:pk>/', VisitorDeletion.as_view(), name='visitor-delete'),
]
