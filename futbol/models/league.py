from django.db import models

# Teams
class League(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")

    def __str__(self):
        return self.name