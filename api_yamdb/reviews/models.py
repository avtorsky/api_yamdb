from django.db import models


class Genre(models.Model):
    """Модель жанра"""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    """Модель произведения"""
    name = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, related_name='titles', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, related_name='titles', on_delete=models.PROTECT)
    year = models.IntegerField()


