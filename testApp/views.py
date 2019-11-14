from django.views import generic
from . models import card_table, image_table, code_table
from django.shortcuts import render

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
        
        imageObj = image_table.objects.filter(cardID = self.cardID_for_txt).order_by('serialNO')
        imageObjIndex = 0

        codeObj = code_table.objects.filter(cardID = self.cardID_for_txt).order_by('serialNO')
        codeObjIndex = 0

        a = str(card_table.objects.get(cardID = self.cardID_for_txt).text)
        ans = []
        aa = a.split('<br><br>')
        if aa[0] != '':
            ans.append(aa[0])
        i = 1
        while i<len(aa):
            ans.append('<br><br>')
            if aa[i] != '':
                ans.append(aa[i])
            i = i+1

        Ans = []
        i = 0
        while i<len(ans):
            aa = ans[i].split('<br>')
            if aa[0] != '':
                Ans.append(aa[0])
            j = 1
            while j<len(aa):
                Ans.append('<br>')
                if aa[j] != '':
                    Ans.append(aa[j])
                j = j+1
            #Ans.append('<br>')
            i = i+1

        ANS = []
        i = 0
        while i<len(Ans):
            aa = Ans[i].split('<img>')
            ANS.append(aa[0])
            j = 1
            while j<len(aa):
                ANS.append(['<img>', imageObj[imageObjIndex]])
                #ANS.append({'id': '<img>','imageObj': imageObj[imageObjIndex]})
                imageObjIndex = imageObjIndex +1
                if len(imageObj) == imageObjIndex:
                    imageObjIndex = 0 
                
                ANS.append(aa[j])
                j = j+1
            i = i+1

        answer = []
        i = 0
        while i<len(ANS):
            if len(ANS[i]) == 2 and ANS[i][0] == '<img>':
                answer.append(ANS[i])
                i = i+1
                continue
            aa = ANS[i].split('<code>')
            answer.append(aa[0])
            j = 1
            while j<len(aa):
                answer.append(['<code>', codeObj[codeObjIndex]])
                #answer.append({'id': '<code>','codeObj': codeObj[codeObjIndex]})
                codeObjIndex = codeObjIndex +1
                if len(codeObj) == codeObjIndex:
                    codeObjIndex = 0 
                
                ANS.append(aa[j])
                j = j+1
            i = i+1

        while len(answer[len(answer)-1])==1 and (answer[len(answer)-1] == '<br>' or answer[len(answer)-1] == ''):
            answer = answer[:-1]

        while len(answer[0])==1 and answer[0] == '':
            answer = answer[1:]
        
        context['list'] = answer
        
        return context