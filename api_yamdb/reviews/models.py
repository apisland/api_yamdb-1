from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

ROLES = [
    'Admin',
    'Moderator',
    'User',
]


class CustomUser(AbstractUser):
    role = models.CharField(
        choices=ROLES,
        default='User',
    )
    bio = models.TextField(max_length=500)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Titles(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    category = models.ForeignKey(Category)


class Reviews(models.Model):
    text = models.CharField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='author',
    )
    title = models.ForeignKey(
        Titles,
        verbose_name='Произведение'
    )
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    pub_date = models.DateTimeField(
        'Опубликовано в:',
        auto_now_add=True,
    )