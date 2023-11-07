from django.views.generic import TemplateView
from futbol.models.goal import Goal
from futbol.models.league import League

from futbol.models.team import Team
from futbol.views.views.schedule_view import ScheduleView
from django.template.loader import render_to_string
from futbol.views.views.standing_view import StandingView

from futbol.views.views.stats_goals_view import StatsGoalsView


class LeaguePageView(TemplateView):
    # model = Team
    template_name = "pages/league_page.html"
    # context_object_name = "team"
    # pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        # Uff lo dejo asi para estudio
        context = super().get_context_data(**kwargs)

        league = League.objects.get(slug=self.kwargs.get('league_slug'))

        schedules_view = ScheduleView(**kwargs)
        schedules_context = schedules_view.get_context_data(request=self.request,  league_slug=self.kwargs.get('league_slug'), limit=5)
        context['schedules'] = render_to_string(schedules_view.template_name, schedules_context)

        stats_goals_view = StatsGoalsView(**kwargs)
        stats_goals_context = stats_goals_view.get_context_data(request=self.request, league_slug=self.kwargs.get('league_slug'), limit=5, show_details=True)
        stats_goals_view = render_to_string(stats_goals_view.template_name, stats_goals_context)
        context['stats_goals_view'] = stats_goals_view
        
        standing_view = StandingView(**kwargs)
        standing_view_context = standing_view.get_context_data(request=self.request, league_slug=self.kwargs.get('league_slug'), limit=8)
        standing_view = render_to_string(standing_view.template_name, standing_view_context)
        context['standing_view'] = standing_view
        
        context['league'] = league
        return context

