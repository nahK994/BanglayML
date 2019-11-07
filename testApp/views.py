from django.views import generic
from . models import cardTableNew

class HomeView(generic.ListView):
    template_name = 'index.html'
    model = cardTableNew

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Introduction - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'Intro').order_by('cardID')
        return context

class SL_View(generic.ListView):
    template_name = 'SL_View.html'
    model = cardTableNew

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Supervised Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'SL').order_by('cardID')
        return context

class UL_View(generic.ListView):
    template_name = 'UL_View.html'
    model = cardTableNew

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Unsupervised Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'UL').order_by('cardID')
        return context

class RL_View(generic.ListView):
    template_name = 'RL_View.html'
    model = cardTableNew

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reinforcement Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = 'RL').order_by('cardID')
        return context

class Text(generic.ListView):
    template_name = 'Text.html'
    model = cardTableNew
    cardID_for_txt = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Text - BanglayML'
        context['querySet'] = cardTableNew.objects.get(cardID = self.cardID_for_txt)
        return context