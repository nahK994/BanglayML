from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class SL_View(TemplateView):
    template_name = "SL_View.html"

class UL_View(TemplateView):
    template_name = "UL_View.html"

class RL_View(TemplateView):
    template_name = "RL_View.html"

class IntroText(TemplateView):
    template_name = "IntroText.html"