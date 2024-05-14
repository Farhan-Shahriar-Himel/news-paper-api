from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.
class CategoryViewSets(viewsets.ModelViewSet):
    queryset = models.CategoryClass.objects.all()
    serializer_class = serializers.CategorySerializer