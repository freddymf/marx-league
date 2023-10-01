from django.views.generic import TemplateView

from futbol.models.schedule import Schedule
from futbol.views.views.schedule_view import ScheduleView
from django.template.loader import render_to_string


class TeamsPageView(TemplateView):
    template_name = "views/teams_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        league_slug = self.kwargs['league_slug']

        # schedules_view = ScheduleView(**kwargs)
        # schedules_context = schedules_view.get_context_data(request=self.request, limits=5, show_details=True)
        # schedules = render_to_string(schedules_view.template_name, schedules_context)

        context['league_slug'] = league_slug
       
        return context