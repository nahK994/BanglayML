from django.urls import path
#from . models import card_table
from . import views

urlpatterns = [
    path('', views.View.as_view(viewType = 'Intro'), name="home"),
    path('SL_View/', views.View.as_view(viewType = 'SL'), name="SL_View"),
    path('UL_View/', views.View.as_view(viewType = 'UL'), name="UL_View"),
    path('RL_View/', views.View.as_view(viewType = 'RL'), name="RL_View"),
]
'''
for i in card_table.objects.all():
    Url = str(i.cardID)+'/'
    urlpatterns += [
        path(Url, views.Text.as_view(cardID_for_txt = i.cardID), name=str(i.cardID)),
    ]
'''
