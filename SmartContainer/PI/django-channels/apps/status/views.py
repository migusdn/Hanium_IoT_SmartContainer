from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import viewsets
from .serializers import DeviceSerializer
from .models import Device
import json


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


def index(request):

    return render(request, 'chat/Status.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
def test(request):
    return render(request,'chat/test.html',{})