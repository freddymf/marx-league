from django.views.generic import TemplateView
from futbol.models.team import Team
from futbol.views.views.schedule_view import ScheduleView
from django.template.loader import render_to_string



class RegulationPageView(TemplateView):
    template_name = "pages/regulation_page.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     teams = Team.objects.all()
    #     context['teams'] = teams

    #     schedules_view = ScheduleView(**kwargs)
    #     schedules_context = schedules_view.get_context_data(request=self.request, _from='today', _to='today')
    #     html = render_to_string(schedules_view.template_name, schedules_context)
    #     # html_code = render(self.request, 'schedule_view.html')

    #     context['schedules'] = html

    #     return context

