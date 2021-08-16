from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    email = serializers.EmailField(
        required=True,
        style={'input_type': 'email', 'placeholder': 'Email will be the username for login'}
    )

    first_name = serializers.CharField(required=True, label="Name")

    last_name = serializers.CharField(required=True, label="Last Name")

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
