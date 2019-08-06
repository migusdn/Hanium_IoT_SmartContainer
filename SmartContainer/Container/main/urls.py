from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
#    path('', views.index, name='index'),

    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('test', TemplateView.as_view(template_name='smain.html'), name='smain'),
    path('map', TemplateView.as_view(template_name="map.html"), name='map'),

    path('sensor', views.sensor, name='sensor'),
    path('container_input', views.container_input, name='container_input'),
]