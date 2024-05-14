from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserRegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    picture = serializers.ImageField(use_url=True)
    profession = serializers.CharField()
    age = serializers.IntegerField()
    institute = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'age', 'profession', 'institute', 'picture']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email'] 
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        picture = self.validated_data['picture']
        profession = self.validated_data['profession']
        age = self.validated_data['age']
        institute = self.validated_data['institute']

        if password != password2:
            raise serializers.ValidationError({'error': "Password Doesn't Exist"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})
        
        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        details = models.UserDetails(user=account, picture=picture, profession=profession, age=age, institute=institute)
        account.set_password(password)
        account.is_active = False
        account.save()
        details.save()
        return account


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleClass
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
