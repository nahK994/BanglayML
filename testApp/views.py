from django.views import generic
from . models import cardTable

class HomeView(generic.ListView):
    template_name = 'index.html'
    model = cardTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Introduction - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'Intro')
        return context

class SL_View(generic.ListView):
    template_name = 'SL_View.html'
    model = cardTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Supervised Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'SL')
        return context

class UL_View(generic.ListView):
    template_name = 'UL_View.html'
    model = cardTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Unsupervised Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'UL')
        return context

class RL_View(generic.ListView):
    template_name = 'RL_View.html'
    model = cardTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reinforcement Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'RL')
        return context

class Text(generic.TemplateView):
    template_name = 'Text.html'