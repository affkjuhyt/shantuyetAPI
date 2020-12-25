from rest_framework import permissions

from userprofile.models import Owner, SecondaryOwner


class OwnerOnly(permissions.BasePermission):
    message = 'Only Owner allowed.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_profile = Owner.objects.filter(user=request.user).first()
            if user_profile:
                return True
        return False


class SecondaryOwnerOnly(permissions.BasePermission):
    message = 'Only Secondary Owner allowed.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_profile = SecondaryOwner.objects.filter(user=request.user).first()
            if user_profile:
                return True
        return False
