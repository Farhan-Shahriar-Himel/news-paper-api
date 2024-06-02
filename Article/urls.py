from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('article', views.ArticleViewSet)
router.register('userlist', views.UserlistView)
router.register('user', views.rawUserView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationViewSet.as_view(), name='register'),
    path('login/', views.UserLoginViewSet.as_view(), name='logIn'),
    path('logout/', views.UserLogoutViewSet.as_view(), name='logOut'),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
]
