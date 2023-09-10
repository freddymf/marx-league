from datetime import date
from django.views.generic import TemplateView
from futbol.models.team import Team
from futbol.models.schedule import Schedule



class LandingPageView(TemplateView):
    template_name = "pages/landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = Team.objects.all()
        context['teams'] = teams


        today = date.today().strftime("%Y-%m-%d")
        print(today)
        schedules = Schedule.objects.filter(date__range=[today, today])
        context['schedules'] = schedules

        return context



            
# def index(request):
#     teams = Team.objects.all()
#     return render(request, 'landing.html', {'teams', teams})



# def main_view(request):
#     navbar_data = get_navbar_data()  # Obtener datos para la barra de navegación
#     sidebar_data = get_sidebar_data()  # Obtener datos para la barra lateral

#     return render(request, 'base.html', {
#         'navbar': render(request, 'navbar.html', navbar_data),
#         'sidebar': render(request, 'sidebar.html', sidebar_data),
#     })