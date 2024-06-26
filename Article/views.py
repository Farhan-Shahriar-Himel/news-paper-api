from rest_framework import viewsets 
from rest_framework.generics import ListAPIView
from . import models
from . import serializers
from Category.models import CategoryClass
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers as serial
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.ArticleClass.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = serializers.ArticleSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug']


class rawUserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UsersSerilalizers


class UserlistView(viewsets.ModelViewSet):
    queryset = models.UserDetails.objects.all()
    serializer_class = serializers.UserListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id']


class UserRegistrationViewSet(APIView):
    serializer_class = serializers.UserRegistrationSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_mail.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your Email for confirmation")
        return Response(serializer.errors)
    

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('logIn')
    else:
        return redirect('register')
    

class UserLoginViewSet(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': "Invalid username or password"})
        return Response(serializer.error)
    

class UserLogoutViewSet(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('logIn')
    

def categoryFilter(request, category_name):
    cat = CategoryClass.objects.get(slug=category_name)
    article = models.ArticleClass.objects.filter(category=cat)
    print(article)
    serialized_article = serial.serialize('json', article)
    return JsonResponse(serialized_article, safe=False)

# class CategoryFilter(APIView):
#     queryset = models.ArticleClass.objects.all()
#     serializer_class = serializers.ArticleSerializers
