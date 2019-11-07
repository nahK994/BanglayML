from django.views import generic
from . models import cardTableNew

class View(generic.ListView):
    template_name = 'index.html'
    model = cardTableNew
    viewType = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.viewType == 'Intro':
            context['title'] = 'Introduction - BanglayML'
        elif self.viewType == 'SL':
            context['title'] = 'Supervised Learning - BanglayML'
        elif self.viewType == 'UL':
            context['title'] = 'Unsupervised Learning - BanglayML'
        elif self.viewType == 'RL':
            context['title'] = 'Reinforcement Learning - BanglayML'
        context['querySet'] = super().get_queryset().filter(categoryID = self.viewType).order_by('cardID')
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