import logging

from rest_framework import status, generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ViewSetMixin
from django.contrib.auth.models import User

from root.authentications import BaseUserJWTAuthentication
from userprofile.models import UserProfile, SecondaryOwner
from userprofile.serializers import UserProfileSerializer

logger = logging.getLogger(__name__.split('.')[0])


class UserPublicView(ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    authentication_classes = [BaseUserJWTAuthentication]
    filter_fields = []
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get_queryset(self):
        return UserProfile.objects.filter(user_id=self.request.user).all()

    def list(self, request, *args, **kwargs):
        user_profile = self.get_queryset().first()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)


class UpdateInfo(ReadOnlyModelViewSet):
    authentication_classes = [BaseUserJWTAuthentication]

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(id=request.user.id).first()

        if User.objects.filter(username=username).exists():
            return Response({'Error': 'Username already exists'})
        else:
            user.username = username
            user.set_password(password)
            user.save()
            secondary_owner = SecondaryOwner.objects.filter(user=user).first()
            secondary_owner.fullname = user.username
            secondary_owner.save()

            return Response({'Success': 'Create user successfully'})