from rest_framework import serializers
from . import models

class UserRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserRatingModel
        fields = '__all__'