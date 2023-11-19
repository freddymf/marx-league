from django.views.generic import TemplateView
from futbol.models.league import League
from futbol.models.player_league_team import PlayerLeagueTeam

from futbol.models.team import Team
from django.template.loader import render_to_string

from futbol.views.views.schedule_view import ScheduleView
from futbol.views.views.stats_goals_view import StatsGoalsView


class TeamDetailsPageView(TemplateView):
    # model = Team
    template_name = "pages/team_details_page.html"
    # context_object_name = "team"
    # pk_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        # Uff lo dejo asi para estudio
        context = super().get_context_data(**kwargs)
        leagues = League.objects.all()

        team = Team.objects.get(slug=kwargs.get("team_slug"))
        league = League.objects.get(slug=kwargs.get("league_slug"))

        players_leagues_teams = PlayerLeagueTeam.objects.filter(
            team=team, league=league, active=True
        )

        schedules_view = ScheduleView(**kwargs)
        schedules_context = schedules_view.get_context_data(
            request=self.request,
            league_slug=self.kwargs.get("league_slug"),
            team_slug=self.kwargs.get("team_slug"),
        )
        context["schedules"] = render_to_string(
            schedules_view.template_name, schedules_context
        )

        stats_goals_view = StatsGoalsView(**kwargs)
        stats_goals_context = stats_goals_view.get_context_data(
            request=self.request,
            league_slug=self.kwargs.get("league_slug"),
            team_slug=self.kwargs.get("team_slug"),
        )
        stats_goals_view = render_to_string(
            stats_goals_view.template_name, stats_goals_context
        )
        
        context["stats_goals_view"] = stats_goals_view

        context["team"] = team
        context["players_leagues_teams"] = players_leagues_teams
        context["league"] = league
        context["leagues"] = leagues

        # context['schedules'] = html
        return context
