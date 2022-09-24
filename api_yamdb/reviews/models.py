from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name
