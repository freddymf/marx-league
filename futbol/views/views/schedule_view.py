from datetime import date
from django.shortcuts import render
from django.views.generic import TemplateView
from futbol.models.team import Team
from futbol.models.schedule import Schedule



class ScheduleView(TemplateView):
    template_name = "views/schedule_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = date.today().strftime("%Y-%m-%d")
        schedules = Schedule.objects.filter(date__range=[today, today])
        context['schedules'] = schedules

        return context