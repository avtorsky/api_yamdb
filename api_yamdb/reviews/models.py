from django.db import models

from .validators import validate_title_year


class Genre(models.Model):
    """Модель жанра"""

    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Метка',
    )

    class Meta:
        ordering = 'name'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(
        max_length=256,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Метка',
    )

    class Meta:
        ordering = 'name'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведения"""

    name = models.CharField(
        max_length=500,
        verbose_name='Произведение',
    )
    year = models.IntegerField(
        validators=(validate_title_year),
        verbose_name='Год выпуска',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Категория',
    )
    rating = models.IntegerField(
        default=None,
        null=True,
        verbose_name='Рейтинг',
    )

    class Meta:
        ordering = 'name'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр',
    )

    class Meta:
        verbose_name_plural = 'Произведения и жанры'

    def __str__(self):
        return f'{self.title}, {self.genre}'
