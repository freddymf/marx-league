from django.views.generic import TemplateView
from futbol.models.goal import Goal

from futbol.models.team import Team
from futbol.views.views.schedule_view import ScheduleView
from django.template.loader import render_to_string


class TeamDetailsPageView(TemplateView):
    model = Team
    template_name = "pages/team_details_page.html"
    context_object_name = "team"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        # Uff lo dejo asi para estudio
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs.get(self.pk_url_kwarg)
        team = self.model.objects.get(id=team_id)
    
        context[self.context_object_name] = team

        players = team.player_set.all()
     
        schedules_view = ScheduleView(**kwargs)
        schedules_context = schedules_view.get_context_data(request=self.request, team_filter=team)
        html = render_to_string(schedules_view.template_name, schedules_context)


        context['team'] = team
        context['players'] = players
        context['schedules'] = html
        return context

