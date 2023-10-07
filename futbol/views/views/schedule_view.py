from datetime import date
from django.views.generic import TemplateView
from django.db.models import Q
from futbol.models.league import League
from futbol.models.schedule import Schedule
from futbol.models.team import Team

class ScheduleView(TemplateView):
    template_name = "views/schedule_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        schedules = Schedule.objects.all()
        if '_from' in kwargs and '_to' in kwargs:
            _from = date.today().strftime("%Y-%m-%d") if kwargs['_from'] == 'today' else kwargs['_from']  
            _to = date.today().strftime("%Y-%m-%d") if kwargs['_to'] == 'today' else kwargs['_to']
            schedules = Schedule.objects.filter(date__range=[_from, _to])
        elif '_from' in kwargs: 
            _from = date.today().strftime("%Y-%m-%d") if kwargs['_from'] == 'today' else kwargs['_from']  
            schedules = Schedule.objects.filter(date__gte=_from)
        elif '_to' in kwargs: 
            _to = date.today().strftime("%Y-%m-%d") if kwargs['_from'] == 'today' else kwargs['_to']  
            schedules = Schedule.objects.filter( date__lte=_to)

            
        if 'team_slug' in kwargs:
            team = Team.objects.get(slug=kwargs['team_slug'])
            schedules = schedules.filter(Q(vs=team) | Q(hc=team))
            context['team'] = team

        if 'league_slug' in kwargs:
            league = League.objects.get(slug=kwargs.get('league_slug'))
            schedules = schedules.filter(league__slug=kwargs.get('league_slug'))
            context['league'] = league

        schedules = schedules.order_by('-date')

        if 'limit' in kwargs:  # limit
            schedules = schedules[:kwargs.get('limit')]


        if 'details' in kwargs:
            context['show_details'] = True

        context['schedules'] = schedules

        return context
