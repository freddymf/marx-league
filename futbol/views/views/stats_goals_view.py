from datetime import date
from django.views.generic import TemplateView
from django.db.models import Q
from futbol.models.goal import Goal
from django.db.models import Sum, Case, When, IntegerField, Count
from futbol.models.league import League

from futbol.models.team import Team

class StatsGoalsView(TemplateView):
    template_name = "views/stats_goals_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        goals = Goal.objects

        if 'league_slug' in kwargs:
            league = League.objects.get(slug=kwargs.get('league_slug'))
            goals = goals.filter(schedule__league=league, player__playerleagueteam__league=league)
            context['league'] = league

        if 'team_slug' in kwargs:
            team = Team.objects.get(slug=kwargs['team_slug'])
            goals = goals.filter(Q(schedule__vs=team) | Q(schedule__hc=team))
            goals = goals.filter(Q(player__playerleagueteam__team=team) & Q(player__playerleagueteam__league=league))                       
            context['team'] = team

        goals = goals.select_related('player', 'player__playerleagueteam__team')

        goals = goals.values('player', 'player__name', 'player__playerleagueteam__team__imagen'
        ).annotate(
            goals=Count('player'),
            penalties=Sum(Case(When(penalty=True, then=1), default=0, output_field=IntegerField()))
        ).order_by('-goals')

        # str = goals.query
        # print(str)

        if 'limit' in kwargs:  # limit
            goals = goals[:kwargs.get('limit')]

        context['goals'] = goals
        
        return context
