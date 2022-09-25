from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

class Title(models.Model):
    category =models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        null=True,
        black=True
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )
    name = models.TextField()
    year = models.IntegerField()
    description = models.TextField(
        null=True,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    text = models.TextField()
    score = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
