import logging

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_registration.exceptions import BadRequest

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
        return UserProfile.objects.filter(user_id=self.request.user.id).all()

    def list(self, request, *args, **kwargs):
        user_profile = self.get_queryset().first()
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)


class UpdateInfo(ReadOnlyModelViewSet):
    authentication_classes = [BaseUserJWTAuthentication]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data['username']
        password = request.data['password']

        username = username.lower()
        if User.objects.filter(username=username).exists():
            return Response({'Error': 'Username already exists'})
        else:
            user = User.objects.filter(id=request.user.id).first()
            user.username = username
            try:
                validate_password(password, user=user)
            except ValidationError as exc:
                raise BadRequest(exc.messages[0])

            user.set_password(password)
            user.save()

            secondary_owner = SecondaryOwner.objects.filter(user=user).first()
            secondary_owner.fullname = user.username
            secondary_owner.save()

            return Response({'Success': 'Create user successfully'})
