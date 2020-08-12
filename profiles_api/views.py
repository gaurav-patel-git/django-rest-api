from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework import filters

from profiles_api import permissions
from . import serializers
from .models import UserProfile, ProfileFeedItem

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = ['hello this is a test api view', 'This is another but in first index']

        return Response({"message":"hello api view", "an_apiview":an_apiview})
        
    def post(self, request):
        """Returns hello name for the post request"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handel Updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handel Partially Updating an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handel Deleting an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Testing API using Viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns hello"""
        a_view = ['this is a response using viewset', 'hope everything is fine']
        return Response({'message':'hello', 'a_view':a_view})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} new'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        """Retrive an object by it's ID"""
        return Response({'HTTP_method':'GET'})
    
    def partial_update(self, request, pk=None):
        """Handel partialling updating an object by it's ID"""
        return Response({'HTTP_method':'PATCH'})
    
    def update(self, request, pk=None):
        """Update an object by it's ID"""
        return Response({'HTTP_method':'PUT'})
    
    def destroy(self, request, pk=None):
        """Delete an object by it's ID"""
        return Response({'HTTP_method':'DELETE'})

class UserProfielViewSet(viewsets.ModelViewSet):
    """Handel creating and updating user profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handel creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileFeedviewSet(viewsets.ModelViewSet):
    """Handel creating and updating user profile feed"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)
