from django.urls import path
from . import consumers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
    path('test/test/', views.test, name='test'),
    path('freeze', views.freeze, name='freeze'),
    path('dohumid', views.dohumid, name='heat'),
    path('uphumid', views.uphumid, name='uphumid'),
  #  path('test', consumers.TestConsumer, name='test')
]