from re import M
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator


class User(AbstractUser):
    """ Модель юзер"""
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER_ROLE = [
        ('user', USER),
        ('admin', ADMIN),
        ('moderator', MODERATOR),
    ]

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Имя пользователя',
        validators=[RegexValidator(
            regex=r'^[\w.@+-_]+$', # проверить как вставить me
            message='Имя не может быть "me".'
        )],
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        validators=[EmailValidator,],
        verbose_name='Электронная почта.',
    )
    first_name = models.TextField(
        max_length=150,
        blank=True,
        )
    last_name = models.TextField(
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        verbose_name='Пару слов о себе',
        blank=True,
    )
    role  = models.CharField(
        max_length=30,
        choices=USER_ROLE,
        default='user',
        verbose_name='Роль',
    )

    @property
    def is_user(self):
        return self.role == self.USER
    
    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', )

        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            ),
        ]


