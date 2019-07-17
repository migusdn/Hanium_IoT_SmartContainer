from django.conf.urls import url
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
#    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('container_input', views.container_input, name='container_input'),
    path('', include('detail.urls')),


]