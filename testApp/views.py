from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class SL_View(TemplateView):
    template_name = "SL_View.html"

class UL_View(TemplateView):
    template_name = "UL_View.html"

class RL_View(TemplateView):
    template_name = "RL_View.html"

class AI_IntroText(TemplateView):
    template_name = "AI_IntroText.html"

class ML_IntroText(TemplateView):
    template_name = "ML_IntroText.html"

class RL_IntroText(TemplateView):
    template_name = "RL_IntroText.html"

class RL_Q_learningText(TemplateView):
    template_name = "RL_Q_learningText.html"

class k_means_clusteringText(TemplateView):
    template_name = "k_means_clusteringText.html"