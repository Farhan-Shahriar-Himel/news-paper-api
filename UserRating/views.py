from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets

# Create your views here.
class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = models.UserRatingModel.objects.all()
    serializer_class = serializers.UserRatingSerializers