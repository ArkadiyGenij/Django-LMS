from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    number = models.CharField(max_length=12, unique=True, verbose_name="контактный номер")
    city = models.CharField(max_length=100, verbose_name="город")
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True, verbose_name="аватарка")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
