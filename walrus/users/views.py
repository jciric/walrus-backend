from django.shortcuts import render, get_object_or_404
# from users.models import users
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer

# Create your views here.

class UserViewList(APIView):
    def get(self, request, format=None):
        queryset = User.objects.all()[:20]
        data = UserSerializer(queryset, many=True).data
        return Response(data)

class UserViewDetail(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(User, pk=pk)
        data = UserSerializer(queryset).data
        return Response(data)
