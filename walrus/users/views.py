from django.shortcuts import render, get_object_or_404
# from users.models import users
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer, UserSerializerDetail
from rest_framework import authentication, permissions

# Create your views here.

class UserViewList(APIView):

    def get(self, request, format=None):
        queryset = User.objects.all()[:20]
        data = UserSerializer(queryset, many=True).data
        return Response(data)

class UserViewDetail(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk):
        queryset = get_object_or_404(User, pk=pk)
        data = UserSerializerDetail(queryset).data
        return Response(data)
