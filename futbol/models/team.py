from django.db import models

from futbol.models.league import League


# Teams
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    # name1 = models.CharField(max_length=100, unique=False, null=True, blank=True)

    grade = models.CharField(max_length=50, null=True, blank=True)
    abbrev = models.CharField(max_length=3, null=True, blank=True)
    imagen = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name
