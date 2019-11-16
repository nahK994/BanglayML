from django.urls import path
from . models import CardsInfo
from . import views

urlpatterns = [
    path('', views.View.as_view(viewType = 'Intro'), name="home"),
    path('SL_View/', views.View.as_view(viewType = 'SL'), name="SL_View"),
    path('UL_View/', views.View.as_view(viewType = 'UL'), name="UL_View"),
    path('RL_View/', views.View.as_view(viewType = 'RL'), name="RL_View"),
    path('<int:cardID_for_txt>/', views.Text),
]