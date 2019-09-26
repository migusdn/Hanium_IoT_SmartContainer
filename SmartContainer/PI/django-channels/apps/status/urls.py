from django.urls import path
from . import consumers
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
    path('test/test/', views.test, name='test'),
    path('dotemp', views.dotemp, name='dot'),
    path('uptemp', views.uptemp, name='upt'),

    path('dohumid', views.dohumid, name='doh'),
    path('uphumid', views.uphumid, name='uph'),
    path('set', views.SetTempHumid, name='setting'),
    path('SetTempHumidAct', views.SetTempHumidAct, name="acting"),
  #  path('test', consumers.TestConsumer, name='test')
]