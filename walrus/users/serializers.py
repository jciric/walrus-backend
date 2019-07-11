from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
