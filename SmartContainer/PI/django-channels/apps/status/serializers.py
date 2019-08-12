from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('ConId', 'Stat', 'Temper', 'Humid', 'Door', 'SetTemper', 'SetHumid', 'UpTemper', 'DoTemper', 'UpHumid', 'DoHumid')
