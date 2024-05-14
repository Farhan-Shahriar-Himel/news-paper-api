from django.db import models
from django.contrib.auth.models import User
from Category.models import CategoryClass
# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='Article/media/uploads', null=True, blank=True)
    profession = models.CharField(max_length=100)
    age = models.IntegerField()
    institute = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
    

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class ArticleClass(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(CategoryClass, on_delete=models.CASCADE)
    publishing_date = models.DateTimeField(auto_now_add=True)
    ratings = models.CharField(choices=STAR_CHOICES, max_length=10)
    picture = models.ImageField(upload_to='Article/media/uploads', null=True, blank=True)

    def __str__(self) -> str:
        return self.headline
