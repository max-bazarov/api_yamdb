from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
