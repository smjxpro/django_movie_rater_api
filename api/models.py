from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, related_name='rating', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
