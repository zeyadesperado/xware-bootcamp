from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import *
from .serializer import *

@api_view(["GET","POST"])
def BookList(request):
    
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookPostSerializer(books, many=True)
    elif request.method == 'POST':
        serializer = BookPostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else :
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response(serializer.data, status=status.HTTP_409_CONFLICT)


@api_view(["PUT","PATCH","DELETE","GET"])
def UpdateBook(request,id):
    books = Book.objects.filter(id = id)
    if request.method == 'GET':
        serializer = BookPostSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if books == None:
        return Response({"details": "this user is not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    partial = False
    if request.method == "PATCH":
        partial = True
    serializer = BookPostSerializer(books, request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(["GET","POST"])
def VisitorList(request):    
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        serializer = VisitorPostSerializer(visitors, many=True)
    elif request.method == 'POST':
        serializer = VisitorPostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else :
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response(serializer.data, status=status.HTTP_409_CONFLICT)


@api_view(["PUT","PATCH","DELETE","GET"])
def UpdateVisitor(request,id):
    visitors = Visitor.objects.filter(id = id)
    if request.method == 'GET':
        serializer = VisitorPostSerializer(visitors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if visitors == None:
        return Response({"details": "this user is not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        visitors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    partial = False
    if request.method == "PATCH":
        partial = True
    serializer = VisitorPostSerializer(visitors, request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
