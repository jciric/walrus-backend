from rest_framework import serializers
from users.models import users

class UserSerializer(serializers.Serializer):
    class Meta:
        model = users
        fields = ('username', 'password', 'email')

    def create(self, validated_data):

        return users.objects.create(instance=users, **validated_data)

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance
