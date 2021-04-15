from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostLikeSerializer,
    PostUnlikeSerializer,
)
from .utils import update_last_request, get_user, count_likes


class PostsView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    lookup_field = 'id'

    def get(self, request, id=None):
        update_last_request(request)
        if id:
            return self.retrieve(request, id)
        return self.list(request, id)


class PostCreateView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        update_last_request(request)
        user = get_user(request)
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'author': user.username,
            'email': user.email
        }
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostLikeView(APIView):
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, id=None):
        update_last_request(request)
        data = {
            'user': get_user(request).id,
            'post': id
        }
        serializer = PostLikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUnlikeView(APIView):
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, id=None):
        update_last_request(request)
        data = {
            'user': get_user(request).id,
            'post': id
        }
        serializer = PostUnlikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnalyticsView(APIView):
    def get(self, request):
        update_last_request(request)
        return Response(count_likes(
            request.query_params['date_from'],
            request.query_params['date_to']
        ))
