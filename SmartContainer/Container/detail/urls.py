from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='detail222.html'), name='Detail'),
#    path('ContainerDetail', views.ContainerDetail, name='ContainerDetail'),
    path('test', views.DetailTest, name='DetailTest'),
]