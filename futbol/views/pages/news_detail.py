from django.views.generic import DetailView
from futbol.models.news import News


class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news_detail.html'
    context_object_name = 'news'