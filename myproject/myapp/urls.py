from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('amk', views.amk, name='amk'),
    path('bedok', views.bedok, name='bedok'),
    path('central', views.central, name='central'),
    path('jurong', views.jurong, name='jurong'),
    path('tanglin', views.tanglin, name='tanglin'),
    path('woodlands', views.woodlands, name='woodlands'),
    path('airport', views.airport, name='airport')

]
