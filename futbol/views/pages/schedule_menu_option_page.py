from django.views.generic import TemplateView

from futbol.models.schedule import Schedule


class ScheduleMenuOptionPageView(TemplateView):
    template_name = "pages/schedule_menu_option_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedules = Schedule.objects.all()

        date_filter = self.request.GET.get('date')
        # team_filter = self.request.GET.get('team')

        if date_filter:
            schedules = schedules.filter(date=date_filter)
        # if team_filter:
        #     schedules = schedules.filter(team=team_filter)

        schedules = schedules.order_by('date')
        context['schedules'] = schedules
        context['context'] = context

        return context