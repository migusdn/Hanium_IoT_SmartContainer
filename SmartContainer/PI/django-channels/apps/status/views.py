from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import viewsets
from .serializers import DeviceSerializer
from .models import Device
import requests
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
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

@csrf_exempt
def freeze(request):
    mode = 'freeze'
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('Client_ip: '+ip)
    url='http://'+ip+':8000/main/sensor'
    res = Device.objects.get(ConId='B1')
    res.EnforceT_Do = True
    res.DoTemper = True
    res.save()
    #전송 쿼리 작성
    paramDict = {
        "ConId": res.ConId,
        "Temper": res.Temper,
        "Humid": res.Humid,
        "Door": "1",
        "SetTemper": res.SetTemper,
        "SetHumid": res.SetHumid,
        "UpTemper": res.UpTemper,
        "DoTemper": res.DoTemper,
        "UpHumid": res.UpHumid,
        "DoHumid": res.DoHumid
    }
    data = "test"
    jsonp_callback = request.GET.get("callback")
    print(jsonp_callback)
    if jsonp_callback:
        response = HttpResponse("%s(%s);" % (jsonp_callback, json.dumps(data)))
        response["Content-type"] = "text/javascript; charset=utf-8"
    else:
        response = HttpResponse(json.dumps(data))
        response["Content-type"] = "application/json; charset=utf-8"
    #params
    requests.get(url, params=paramDict)
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'status',
        {
            'con_type': 'freeze',
            'type': 'chat_message',
            'message': 'true'
        }
    )

    return HttpResponse("%s(%s);" % (jsonp_callback, json.dumps(data)))
