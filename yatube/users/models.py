from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email'), unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=255, unique=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=255, unique=False)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # def save(self, *args, **kwargs):
    #     # вызываем метод set_password(), чтобы установить пароль
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)

