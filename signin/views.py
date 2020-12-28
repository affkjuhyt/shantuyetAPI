
import requests
from django.contrib.auth import authenticate
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from root import settings
from signin.serializers import UserLoginSerializer
from userprofile.models import UserProfile, SecondaryOwner

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

FACEBOOK_DEBUG_TOKEN_URL = "https://graph.facebook.com/debug_token"
FACEBOOK_ACCESS_TOKEN_URL = "https://graph.facebook.com/v7.0/oauth/access_token"
FACEBOOK_URL = "https://graph.facebook.com/"


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()
            secondary_owner = SecondaryOwner(user=user)
            secondary_owner.fullname = user.username
            secondary_owner.user_type = 'secondary_owner'
            secondary_owner.save()

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response['username'] = user.username
        response['access_token'] = str(token)
        return Response(response)


class FacebookView(APIView):
    def post(self, request):
        user_info_url = FACEBOOK_URL + request.data.get("id")
        print(request.data.get("id"), request.data.get("token"))
        user_info_payload = {
            "fields": "id,name",
            "access_token": request.data.get("token"),
        }

        user_info_request = requests.get(user_info_url, params=user_info_payload)
        user_info_response = json.loads(user_info_request.text)

        try:
            user = User.objects.get(email=user_info_response["id"])
        except User.DoesNotExist:
            user = User()
            user.username = user_info_response["id"]
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = user_info_response["id"]
            user.save()
            secondary_owner = SecondaryOwner(user=user)
            secondary_owner.fullname = user.username
            secondary_owner.user_type = 'secondary_owner'
            secondary_owner.save()

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response["username"] = user.username
        response["access_token"] = str(token)
        return Response(response)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                    'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Email or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
