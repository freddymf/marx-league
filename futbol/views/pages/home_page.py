from django.views.generic import TemplateView
from futbol.models.league import League
from futbol.models.team import Team
from futbol.views.views.schedule_view import ScheduleView
from django.template.loader import render_to_string



class HomePageView(TemplateView):
    template_name = "pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = Team.objects.all()
        context['teams'] = teams

        league = League.objects.get(slug='liga')  # Es el tornero actual

        schedules_view = ScheduleView(**kwargs)
        schedules_context = schedules_view.get_context_data(request=self.request, _from='today', limits=5)
        html = render_to_string(schedules_view.template_name, schedules_context)
        # html_code = render(self.request, 'schedule_view.html')

        context['schedules'] = html
        context['league'] = league

        return context

