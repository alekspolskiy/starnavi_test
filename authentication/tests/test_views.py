from django.urls import reverse
from .test_setup import TestSetUp
from authentication.models import User


class TestViews(TestSetUp):
    def auth(self):
        self.client.post(self.signup_url, self.user_data)
        response = self.client.post(
            self.login_url,
            self.user_data,
            format='json'
        )
        access_token = response.json().get('token').get('access')
        return self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def create_post(self):
        post_data = {
            'title': 'test_title',
            'content': 'test_content'
        }
        response = self.client.post(
            self.create_post_url,
            post_data,
            format='json'
        )
        return response

    def test_user_cant_signup_with_no_data(self):
        response = self.client.post(self.signup_url)
        self.assertEqual(response.status_code, 400)

    def test_user_cant_signup_with_exists_data(self):
        self.auth()
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 400)

    def test_user_can_signup(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 201)

    def test_user_cant_login_with_invalid_credentials(self):
        response = self.client.post(
            self.login_url,
            self.user_data,
            format='json'
        )
        self.assertEqual(response.status_code, 401)

    def test_user_can_login(self):
        self.client.post(self.signup_url, self.user_data)
        response = self.client.post(
            self.login_url,
            self.user_data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_user_get_tokens_after_login(self):
        self.client.post(self.signup_url, self.user_data)
        response = self.client.post(
            self.login_url,
            self.user_data,
            format='json'
        )
        self.assertEqual(response.json().get('token') != '', True)

    def test_user_can_refresh_token(self):
        self.client.post(self.signup_url, self.user_data)
        response = self.client.post(
            self.login_url,
            self.user_data,
            format='json'
        )
        refresh_token = response.json().get('token').get('refresh')
        data = {
            'refresh': refresh_token
        }
        response = self.client.post(
            self.refresh_token_url,
            data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_user_can_get_users_with_token_auth(self):
        self.auth()
        response = self.client.get(
            self.get_users_url,
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_user_cant_get_users_without_token_auth(self):
        self.client.post(self.signup_url, self.user_data)
        self.client.post(
            self.login_url,
            self.user_data,
            format='json'
        )
        response = self.client.get(
            self.get_users_url,
            format='json'
        )

        self.assertEqual(response.status_code, 401)

    def test_user_can_get_user_with_token_auth(self):
        self.auth()
        url = self.get_user_url.format(user_id=User.objects.first().id)
        response = self.client.get(
            url,
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_user_can_create_post(self):
        self.auth()
        response = self.create_post()
        self.assertEqual(response.status_code, 201)

    def test_user_can_get_posts(self):
        self.auth()
        response = self.client.get(
            self.get_posts_url,
            format='json'
        )

        self.assertEqual(response.status_code, 200)

    def test_user_can_like_post(self):
        self.auth()
        response = self.create_post()
        url = self.like_post_url.format(post_id=response.json().get('id'))
        response = self.client.post(
            url,
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_user_can_unlike_post(self):
        self.auth()
        response = self.create_post()
        url = self.unlike_post_url.format(post_id=response.json().get('id'))
        response = self.client.post(
            url,
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_user_can_get_analytics(self):
        self.auth()
        params = {
            'date_from': '2021-4-11',
            'date_to': '2021-4-15'
        }
        response = self.client.get(
            self.analytics_url,
            params,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
