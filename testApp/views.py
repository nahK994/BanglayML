from django.views import generic
from . models import card_table_new

class View(generic.ListView):
    template_name = 'index.html'
    model = card_table_new
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
        context['querySet'] = super().get_queryset().filter(categoryID = self.viewType).order_by('serialNO')
        return context

class Text(generic.ListView):
    template_name = 'Text.html'
    model = card_table_new
    cardID_for_txt = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Text - BanglayML'
        context['querySet'] = card_table_new.objects.get(cardID = self.cardID_for_txt)
        return context