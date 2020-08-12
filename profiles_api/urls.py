from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfielViewSet)
router.register('feed', views.UserProfileFeedviewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-api'),
    path('login/', views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]