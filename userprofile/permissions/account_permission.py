from rest_framework import permissions

from userprofile.models import Owner, SecondaryOwner, Government


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


class GovernmentOnly(permissions.BasePermission):
    message = 'Only Government allowed.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_profile = Government.objects.filter(user=request.user).first()
            if user_profile:
                return True
        return False
