from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=65, unique=True)

    def __str__(self) -> str:
        return self.name
