from django.db.models.signals import post_save
from authentication.models import User
from .models import (
    Post,
    UsersPosts,
    UsersPostsLikes,
    UsersPostsUnlikes,
)


def create_user_posts(sender, instance, created, **kwargs):
    if created:
        UsersPosts.objects.create(
            user=User.objects.filter(id=instance.author.id).first(),
            post=instance
        )


def send_like_post_save(sender, instance, **kwargs):
    instance.post.like += 1
    instance.post.save(force_update=True)


def send_unlike_post_save(sender, instance, **kwargs):
    instance.post.unlike += 1
    instance.post.save(force_update=True)


def delete_unlike_post_save(sender, instance, **kwargs):
    unliked_posts = [
        {
            'post': obj.post_id,
            'user': obj.user_id
        }
        for obj in UsersPostsUnlikes.objects.all()
    ]
    request_data = {
        'post': instance.post.id,
        'user': instance.user.id
    }
    if request_data in unliked_posts:
        instance.post.unlike -= 1
        UsersPostsUnlikes.objects.filter(
            post=instance.post.id,
            user=instance.user.id
        ).first().delete()
    instance.post.save(force_update=True)


def delete_like_post_save(sender, instance, **kwargs):
    liked_posts = [
        {
            'post': obj.post_id,
            'user': obj.user_id
        }
        for obj in UsersPostsLikes.objects.all()
    ]
    request_data = {
        'post': instance.post.id,
        'user': instance.user.id
    }
    if request_data in liked_posts:
        instance.post.like -= 1
        UsersPostsLikes.objects.filter(
            post=instance.post.id,
            user=instance.user.id
        ).first().delete()
    instance.post.save(force_update=True)


post_save.connect(create_user_posts, sender=Post)
post_save.connect(send_like_post_save, sender=UsersPostsLikes)
post_save.connect(delete_unlike_post_save, sender=UsersPostsLikes)
post_save.connect(delete_like_post_save, sender=UsersPostsUnlikes)
post_save.connect(send_unlike_post_save, sender=UsersPostsUnlikes)
