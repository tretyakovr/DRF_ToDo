from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=20, blank=False, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=20, blank=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=20, blank=False)
    email = models.EmailField(verbose_name='e-mail', unique=True)

    class Meta:
        db_table = 'Users'
        verbose_name = 'Пользоаатели'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
