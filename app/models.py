from django.db import models
from django.db.models.signals import post_save
from authentication.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255, default=None)
    author_username = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=100, default=None)
    date = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    unlike = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title


class UsersPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_posts'
        unique_together = ('user', 'post')


class UsersPostsLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
        unique_together = ('user', 'post')


class UsersPostsUnlikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'unlikes'
        unique_together = ('user', 'post')
