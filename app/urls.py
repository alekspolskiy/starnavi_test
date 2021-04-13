from django.urls import path
from .views import PostsListView, PostDetailView

urlpatterns = [
    path('posts/', PostsListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]