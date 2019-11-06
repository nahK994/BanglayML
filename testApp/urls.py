from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('SL_View/', views.SL_View.as_view(), name="SL_View"),
    path('UL_View/', views.UL_View.as_view(), name="UL_View"),
    path('RL_View/', views.RL_View.as_view(), name="RL_View"),
    path('Text/', views.Text.as_view(), name="Text"),
]