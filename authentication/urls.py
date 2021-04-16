from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignUpView, LoginView, UsersView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:id>/', UsersView.as_view(), name='user'),
]
