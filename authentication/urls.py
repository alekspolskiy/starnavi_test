from django.urls import path
from .views import SignUpView, LoginView, UsersListView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UsersListView.as_view()),
]
