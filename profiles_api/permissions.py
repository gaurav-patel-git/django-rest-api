from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiel"""

    def has_object_permission(self, request, view, obj):
        """Cheks user is trying to update their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their status"""

    def has_object_permission(self, request, view, obj):
        """Cheks user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS: 
            return True
        return obj.user_profile.id == request.user.id
        