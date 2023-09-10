from django.db import models
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
        Team, on_delete=models.SET_NULL, related_name="vs_schedule", null=True
    )
    hc = models.ForeignKey(
        Team, on_delete=models.SET_NULL, related_name="hc_schedule", null=True
    )
    date = models.DateField(null=True)
    vs_gol = models.IntegerField(null=True)
    hc_gol = models.IntegerField(null=True)

    points = models.IntegerField(null=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )

    stages = models.CharField(
        max_length=20, choices=STAGES_CHOICES, default="regular"
    )
