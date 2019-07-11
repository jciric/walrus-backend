from rest_framework import serializers
from core.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'owner')

class ContentSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
