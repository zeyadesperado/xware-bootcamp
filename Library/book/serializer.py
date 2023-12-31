from rest_framework import serializers
from .models import *


class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class VisitorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'



class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'