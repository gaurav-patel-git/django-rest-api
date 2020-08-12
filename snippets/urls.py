from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


urlpatterns = [
    path('', include(router.urls)),
]