from django.db import models

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

    def __str__(self) -> str:
        return self.name

