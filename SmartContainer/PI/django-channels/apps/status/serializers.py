from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('status', 'temper', 'humid', 'door', 'settemper', 'sethumid', 'uptemper', 'dotemper', 'uphumid', 'dohumid')
