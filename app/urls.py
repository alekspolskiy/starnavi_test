from django.urls import path
from .views import PostsView, PostLikeView, PostCreateView, PostUnlikeView, AnalyticsView

urlpatterns = [
    path('posts/<int:id>/', PostsView.as_view()),
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/create/', PostCreateView.as_view(), name='create_post'),
    path('posts/<int:id>/like/', PostLikeView.as_view(), name='like_post'),
    path('posts/<int:id>/unlike/', PostUnlikeView.as_view(), name='unlike_post'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]
