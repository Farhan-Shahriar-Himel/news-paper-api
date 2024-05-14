from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SubscriberModel(models.Model):
    Author = models.ForeignKey(User, related_name="author_subscription", on_delete=models.CASCADE)
    Subscriber = models.ForeignKey(User, related_name="user_subscription", on_delete=models.CASCADE)