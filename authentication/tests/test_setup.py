from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.refresh_token_url = reverse('refresh_token')
        self.get_users_url = reverse('users')
        self.get_user_url = '/api/v1/users/{user_id}/'
        self.get_posts_url = reverse('posts')
        self.create_post_url = reverse('create_post')
        self.like_post_url = '/api/v1/posts/{post_id}/like/'
        self.unlike_post_url = '/api/v1/posts/{post_id}/unlike/'
        self.analytics_url = reverse('analytics')

        self.user_data = {
            'username': 'test',
            'email': 'test@gmail.com',
            'password': 'test'
        }

        return super().setUp()
