from django.urls import path,include
from Blog.views import *
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets

router = DefaultRouter()
router.register(r'blogs',BlogViewSet)
urlpatterns = [
    path('', include(router.urls),name='blogs')
]