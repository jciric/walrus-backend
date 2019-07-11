from django.shortcuts import render
from django.contrib.auth import authenticate, login
from core.models import Content

# Create your views here.
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#             ...
#     else:
#         # Return an 'invalid login' error message.
#
#

def add_post(request):
    if request.method == 'POST':
        Content.save()

def delete(request, pk):
    if request.method == 'POST':
        post = Content.get(pk=pk)
        post.delete()

from django.shortcuts import render, get_object_or_404
from core.models import Content
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import ContentSerializer, ContentSerializerDetail
from rest_framework import authentication, permissions

# Create your views here.

class ContentViewList(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        queryset = Content.objects.all()[:20]
        data = ContentSerializer(queryset, many=True).data
        return Response(data)

class ContentViewDetail(APIView):

    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, pk):
        queryset = get_object_or_404(Content, pk=pk)
        data = ContentSerializerDetail(queryset).data
        return Response(data)

class ContentViewDetailofUser(APIView):
    # 
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, pk, owner):
        queryset = get_object_or_404(Content, pk=pk, owner=owner)
        data = ContentSerializerDetail(queryset).data
        return Response(data)
