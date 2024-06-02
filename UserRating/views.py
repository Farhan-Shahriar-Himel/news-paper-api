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
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        news_id = serializers.validate_data['news_id']
        rating = serializers.validate_data['rating']
        # user = self.request.user
        try:
            user = self.request.user
        except:
            print("User not found")
        print(user)
        return
        # news = ArticleClass.objects.get(id=news_id)
        # rating_instance = models.UserRatingModel.objects.create(user=user.id, news=news, rating=rating)
        # return Response({
        #     'data': rating_instance
        # }, status=status.HTTP_201_CREATED)
