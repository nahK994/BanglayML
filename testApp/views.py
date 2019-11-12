from django.views import generic
from . models import card_table, image_table

class View(generic.ListView):
    template_name = 'index.html'
    model = card_table
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
    model = card_table
    cardID_for_txt = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(card_table.objects.get(cardID = self.cardID_for_txt).title)
        context['text'] = str(card_table.objects.get(cardID = self.cardID_for_txt).text)

        obj = image_table.objects.filter(cardID = self.cardID_for_txt)
        for i in obj:
            context[i.title] = i.upload.url
        return context