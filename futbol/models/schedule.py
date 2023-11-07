from django.db import models

from .player import Player
from .team import Team
from .league import League


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

    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

    vs = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name="vs_schedule",
        null=True,
        blank=True,
    )

    hc = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name="hc_schedule",
        null=True,
        blank=True,
    )
    date = models.DateField(null=True, blank=True)

    vs_goals = models.IntegerField(null=True, blank=True, default=0)
    hc_goals = models.IntegerField(null=True, blank=True, default=0)

    vs_definition_penalties = models.IntegerField(null=True, blank=True, default=0)
    hc_definition_penalties = models.IntegerField(null=True, blank=True, default=0)

    vs_points = models.IntegerField(null=True, blank=True, default=0)
    hc_points = models.IntegerField(null=True, blank=True, default=0)

    mvp = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )

    stages = models.CharField(max_length=20, choices=STAGES_CHOICES, default="regular")


    def __str__(self):
        return str(self.league.name) + ': ' + self.hc.name + ' - ' + self.vs.name + ' - ' + self.date.strftime("%d %B")