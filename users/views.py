import json
import logging

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()


@csrf_exempt
@api_view(["GET"])
# @permission_classes((IsAuthenticated,))
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(["GET"])
# @permission_classes((IsAuthenticated,))
def user_detail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@csrf_exempt
@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@csrf_exempt
@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def user_update(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@csrf_exempt
@api_view(["DELETE"])
# @permission_classes((IsAuthenticated,))
def user_delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("User is deleted.")


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
