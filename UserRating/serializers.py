from rest_framework import serializers
from . import models
from Article.models import User, ArticleClass
from Article.serializers import ArticleSerializers, UsersSerilalizers

class UserRatingSerializers(serializers.ModelSerializer):
    # user = UsersSerilalizers(many=False, read_only=True)
    news = ArticleSerializers(many=False, read_only=True)
    news_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.UserRatingModel
        fields = [ 'news', 'news_id', 'rating']

