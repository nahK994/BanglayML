from django.urls import path
from . models import cardTableNew
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('SL_View/', views.SL_View.as_view(), name="SL_View"),
    path('UL_View/', views.UL_View.as_view(), name="UL_View"),
    path('RL_View/', views.RL_View.as_view(), name="RL_View"),
]

for i in cardTableNew.objects.all():
    Url = str(i.cardID)+'/'
    urlpatterns += [
        path(Url, views.Text.as_view(cardID_for_txt = i.cardID), name=str(i.cardID)),
    ]