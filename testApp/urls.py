from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('SL_View/', views.SL_View.as_view(), name="SL_View"),
    path('UL_View/', views.UL_View.as_view(), name="UL_View"),
    path('RL_View/', views.RL_View.as_view(), name="RL_View"),
    path('AI_IntroText/', views.AI_IntroText.as_view(), name="AI_IntroText"),
    path('ML_IntroText/', views.ML_IntroText.as_view(), name="ML_IntroText"),
    path('RL_IntroText/', views.RL_IntroText.as_view(), name="RL_IntroText"),
    path('RL_Q_learningText/', views.RL_Q_learningText.as_view(), name="RL_Q_learningText"),
    path('k_means_clusteringText/', views.k_means_clusteringText.as_view(), name="k_means_clusteringText"),
    path('pcaText/', views.pcaText.as_view(), name="pcaText"),
    path('DQN_IntroText/', views.DQN_IntroText.as_view(), name="DQN_IntroText"),
    path('DQN_TrainingText/', views.DQN_TrainingText.as_view(), name="DQN_TrainingText"),
    path('LinearRegressionText/', views.LinearRegressionText.as_view(), name="LinearRegressionText"),
    path('LogisticRegressionText/', views.LogisticRegressionText.as_view(), name="LogisticRegressionText"),
    path('knnText/', views.knnText.as_view(), name="knnText")
]