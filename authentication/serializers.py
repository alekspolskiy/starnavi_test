from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        if not username.isalnum():
            raise serializers.ValidationError()
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=4, write_only=True)
    username = serializers.CharField(max_length=100, min_length=1)
    get_tokens = serializers.CharField(max_length=100, min_length=1, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'get_tokens']

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')

        return {
            'username': user.username,
            'token': user.get_tokens()
        }
