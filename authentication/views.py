from rest_framework import generics, status, permissions, mixins
from rest_framework.response import Response
from datetime import datetime
from .models import User
from .serializers import SignUpSerializer, LoginSerializer, UsersListSerializer
from app.utils import update_last_request


class UsersListView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        update_last_request(request)
        return self.list(request)


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
