from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API view"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Seializes am object of User Profile"""
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    def create(self, validated_data):
        """Create a user for user profile using custom manager"""
        user = UserProfile.objects.create_user(
                name = validated_data.get('name'),
                email = validated_data.get('email'),
                password = validated_data.get('password')
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes Profile Feed item"""
    
    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}