from django.db import models
from datetime import datetime
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Please enter username')
        if not email:
            raise TypeError('Please enter email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if not password:
            raise TypeError('Please type password')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_request = models.DateTimeField(default=None, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def update_last_request(self):
        self.last_request = datetime.utcnow()
        super(User, self).save()

    def get_tokens(self):
        token = RefreshToken.for_user(self)
        return {
            'refresh': str(token),
            'access': str(token.access_token)
        }
