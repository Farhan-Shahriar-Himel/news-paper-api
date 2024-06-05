from rest_framework import serializers
from . import models
from Article.models import User, ArticleClass
from Article.serializers import ArticleSerializers, UsersSerilalizers

class UserRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserRatingModel
        fields = '__all__'

