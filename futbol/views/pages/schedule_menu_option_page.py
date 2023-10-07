from django.views.generic import TemplateView
from futbol.models.league import League

from futbol.models.schedule import Schedule
from futbol.views.views.schedule_view import ScheduleView
from django.template.loader import render_to_string


class ScheduleMenuOptionPageView(TemplateView):
    template_name = "pages/schedule_menu_option_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        league = League.objects.get(slug=self.kwargs.get('league_slug'))

        schedules_view = ScheduleView(**kwargs)
        schedules_context = schedules_view.get_context_data(request=self.request, league_slug=self.kwargs.get('league_slug'), limits=5, show_details=True)
        schedules = render_to_string(schedules_view.template_name, schedules_context)

        context['schedules'] = schedules
        context['league'] = league

       
        return context