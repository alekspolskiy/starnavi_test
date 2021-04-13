from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt import serializers
from datetime import datetime
from .models import User
from .serializers import SignUpSerializer, LoginSerializer


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(username=request.data.get('username')).first()
        user.last_login = datetime.utcnow()
        user.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
