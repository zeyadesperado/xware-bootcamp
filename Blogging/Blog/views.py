from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, serializers
from rest_framework import filters
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .filters import *
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    ordering_fields = ['-pub_date']
    filter_backends=[DjangoFilterBackend, filters.OrderingFilter , filters.SearchFilter]
    filterset_class = PostFilter
    search_fields = ['first_name']

