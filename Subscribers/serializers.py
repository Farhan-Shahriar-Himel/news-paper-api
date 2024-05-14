from rest_framework import serializers
from . import models

class SubscribersSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SubscriberModel
        fields = '__all__'