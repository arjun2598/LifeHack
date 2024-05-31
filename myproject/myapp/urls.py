from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map0', views.map0, name='map0'),
    path('map1', views.map1, name='map1'),
    path('map2', views.map2, name='map2'),
    path('map3', views.map3, name='map3'),
    path('map4', views.map4, name='map4'),
    path('map5', views.map5, name='map5'),
    path('map6', views.map6, name='map6')

]
