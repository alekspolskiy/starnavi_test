from rest_framework import serializers
from .models import Post, UsersPostsLikes, UsersPostsUnlikes


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'email', 'date']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPostsLikes
        fields = '__all__'


class PostUnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPostsUnlikes
        fields = '__all__'
