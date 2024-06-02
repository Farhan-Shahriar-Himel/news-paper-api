from django.db import models
from django.contrib.auth.models import User
from Article.models import ArticleClass, STAR_CHOICES
# Create your models here.
class UserRatingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(ArticleClass, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.news.headline
