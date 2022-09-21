from django.db import models


# Create your models here.
class Genres(models.Model):
    name = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name
