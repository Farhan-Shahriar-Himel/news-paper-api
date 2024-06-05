from django.shortcuts import render
from . import serializers
from . import models
from Article.models import ArticleClass
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Create your views here.
class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = models.UserRatingModel.objects.all()
    serializer_class = serializers.UserRatingSerializers
    filterset_fields = ['news__id']