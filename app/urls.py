from django.urls import path
from .views import PostsView, PostLikeView, PostCreateView, PostUnlikeView, AnalyticsView

urlpatterns = [
    path('posts/<int:id>/', PostsView.as_view()),
    path('posts/', PostsView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/<int:id>/like/', PostLikeView.as_view()),
    path('posts/<int:id>/unlike/', PostUnlikeView.as_view()),
    path('analitics/', AnalyticsView.as_view()),
]
