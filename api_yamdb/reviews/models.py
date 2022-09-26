from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


TEXT_LENGTH: str = 15


class Genre(models.Model):
    name = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


# class Review(models.Model):
#     text = models.TextField()
#     score = models.IntegerField(
#         default=1,
#         validators=[MinValueValidator(1), MaxValueValidator(10)]
#     )
#     author = models.ForeignKey(
#         'users.User',
#         on_delete=models.CASCADE,
#         related_name='reviews'
#     )
#     pub_date = models.DateTimeField(auto_now_add=True)
#     title = models.ForeignKey(
#         'Title',
#         on_delete=models.CASCADE,
#         related_name='reviews'
#     )

#     def __str__(self) -> str:
#         return self.text[:TEXT_LENGTH]


# class Comment(models.Model):
#     text = models.TextField()
#     author = models.ForeignKey(
#         'users.User',
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     review = models.ForeignKey(
#         Review,
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     pub_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
