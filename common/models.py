from django.db import models


# Teams
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    grade = models.CharField(max_length=50, null=True)
    abbrev = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name


# PLayers
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Nombre")
    grade = models.CharField(max_length=50, null=True)

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# Schedules
class Schedule(models.Model):
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("scheduled", "Scheduled"),
        ("raining", "Raining"),
        ("playing", "Playing"),
        ("pending", "Pending"),
    ]
    STAGES_CHOICES = [
        ("regular", "Regular"),
        ("octavos", "Octavos"),
        ("cuartos", "Cuartos"),
        ("semifinal", "SemiFinal"),
        ("final", "Final"),
    ]

    vs = models.ForeignKey(
        Team, on_delete=models.SET_NULL, related_name="vs_schedule", null=True
    )
    hc = models.ForeignKey(
        Team, on_delete=models.SET_NULL, related_name="hc_schedule", null=True
    )
    date = models.DateField(null=True)
    vs_gol = models.IntegerField(null=True)
    hc_gol = models.IntegerField(null=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )

    stages = models.CharField(
        max_length=20, choices=STAGES_CHOICES, default="regular"
    )

