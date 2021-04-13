import jwt
from rest_framework import generics, permissions, mixins
from .models import Post
from .serializers import PostSerializer
from authentication.models import User


class PostsListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user_id = jwt.decode(
            request.headers.get('Authorization').split(' ')[-1],
            options={"verify_signature": False}
        ).get('user_id')
        user = User.objects.filter(id=user_id).first()
        user.update_last_request()
        return self.list(request)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
