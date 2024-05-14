from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class SubscirbersVieSet(viewsets.ModelViewSet):
    queryset = models.SubscriberModel.objects.all()
    serializer_class = serializers.SubscribersSerializers
    permission_classes = [IsAuthenticated]
