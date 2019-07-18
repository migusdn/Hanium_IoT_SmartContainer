from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/status/<room_name>/', consumers.StatusConsumer),
    path('ws/status/', consumers.AllStatusConsumer),
    path('ws/device/<device_num>/', consumers.DeviceConsumer),
]

