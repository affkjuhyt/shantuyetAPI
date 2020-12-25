from rest_framework import permissions

from userprofile.models import UserProfile


class OwnerOnly(permissions.BasePermission):
    message = 'Only Owner allowed.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.filter(user=request.user).first()
            if user_profile and user_profile.user_type == 'owner':
                return True
        return False


class SecondaryOwnerOnly(permissions.BasePermission):
    message = 'Only Secondary Owner allowed.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.filter(user=request.user).first()
            if user_profile and user_profile.user_type == 'secondary_owner':
                return True
        return False
