from django.db import models

from futbol.models.league import League
from futbol.models.schedule import Schedule
from futbol.models.team import Team

from django.db.models import Sum, F


# Teams
class Standing(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    # name1 = models.CharField(max_length=100, unique=False, null=True, blank=True)

    league = models.ForeignKey(
        League,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    pos = models.IntegerField(null=True, blank=True)
    pj = models.IntegerField(null=True, blank=True)
    pg = models.IntegerField(null=True, blank=True)
    pe = models.IntegerField(null=True, blank=True)
    pp = models.IntegerField(null=True, blank=True)
    pts = models.IntegerField(null=True, blank=True)

    gf = models.IntegerField(null=True, blank=True)
    gc = models.IntegerField(null=True, blank=True)
    gdif = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.league) + " - " + str(self.team)

    @staticmethod
    def update_stat_form_league(request, obj, form, change):
        # Your logic for updating the stat from the league
        # You can access the request, obj, form, and change parameters here
        # Add your code here

        # Example code:
        league = obj.league
        # Actualizar los puntos, partidos ganados y partidos perdidos para cada equipo en la liga
        # teams = Team.objects.filter(league=league)
        teams = Schedule.objects.filter(league=league).values_list("vs", "hc")
        teams = teams.distinct()
        team_ids = set()
        for team in teams:
            team_ids.add(team[0])
            team_ids.add(team[1])
        teams = Team.objects.filter(id__in=team_ids)

        for team in teams:
            # Calcular los puntos, partidos ganados y partidos perdidos para el equipo
            # vs_points = Schedule.objects.filter(league=league, vs=team).aggregate(
            #     Sum("vs_points")
            # )["vs_points__sum"]
            # hc_points = Schedule.objects.filter(league=league, hc=team).aggregate(
            #     Sum("hc_points")
            # )["hc_points__sum"]
            # pts = vs_points or 0 + hc_points or 0

            # Partidos ganados
            pg = (
                Schedule.objects.filter(vs=team, league=league, stages="regular")
                .annotate(
                    vs_total_goals=Sum(F("vs_goals") + F("vs_definition_penalties")),
                    hc_total_goals=Sum(F("hc_goals") + F("hc_definition_penalties")),
                )
                .filter(vs_total_goals__gt=F("hc_total_goals"))
                .count()
                + Schedule.objects.filter(hc=team, league=league, stages="regular")
                .annotate(
                    vs_total_goals=Sum(F("vs_goals") + F("vs_definition_penalties")),
                    hc_total_goals=Sum(F("hc_goals") + F("hc_definition_penalties")),
                )
                .filter(hc_total_goals__gt=F("vs_total_goals"))
                .count()
            )

            # Partidos perdidos
            pp = (
                Schedule.objects.filter(vs=team, league=league, stages="regular")
                .annotate(
                    vs_total_goals=Sum(F("vs_goals") + F("vs_definition_penalties")),
                    hc_total_goals=Sum(F("hc_goals") + F("hc_definition_penalties")),
                )
                .filter(vs_total_goals__lt=F("hc_total_goals"))
                .count()
                + Schedule.objects.filter(hc=team, league=league, stages="regular")
                .annotate(
                    vs_total_goals=Sum(F("vs_goals") + F("vs_definition_penalties")),
                    hc_total_goals=Sum(F("hc_goals") + F("hc_definition_penalties")),
                )
                .filter(hc_total_goals__lt=F("vs_total_goals"))
                .count()
            )

            pe = (
                Schedule.objects.filter(vs=team, league=league, stages="regular")
                .annotate(
                    vs_total_goals=Sum(F("vs_goals") + F("vs_definition_penalties")),
                    hc_total_goals=Sum(F("hc_goals") + F("hc_definition_penalties")),
                )
                .filter(vs_total_goals__exact=F("hc_total_goals"))
                .count()
                + Schedule.objects.filter(hc=team, league=league, stages="regular")
                .annotate(
                    vs_total_goals=Sum(F("vs_goals") + F("vs_definition_penalties")),
                    hc_total_goals=Sum(F("hc_goals") + F("hc_definition_penalties")),
                )
                .filter(hc_total_goals__exact=F("vs_total_goals"))
                .count()
            )

#     gf = Schedule.objects.filter(
#     Q(vs=team) | Q(hc=team),
#     league=league,
#     stages="regular"
# ).aggregate(goals_sum=Sum("vs_goals") + Sum("hc_goals")).get("goals_sum", 0) or 0
            

            # Actualizar los campos pts, pg y pp en el objeto Stat correspondiente al equipo
            try:
                stat_obj = Standing.objects.get(league=league, team=team)
            except Standing.DoesNotExist:
                stat_obj = Standing(league=league, team=team)
            # stat_obj.pts = pts
            stat_obj.pj = pg + pp + pe
            stat_obj.pg = pg
            stat_obj.pp = pp
            stat_obj.pe = pe
            stat_obj.pts = (pg * 3) + pe
            # 
            # stat_obj.gf = gf
            stat_obj.save()
