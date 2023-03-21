from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    _meta = None
    username = None
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=255, unique=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=255, unique=False)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


