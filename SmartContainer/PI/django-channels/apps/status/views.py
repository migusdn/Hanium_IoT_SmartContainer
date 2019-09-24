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
    return render(request, 'chat/test.html', {})


@csrf_exempt
def freeze(request):
    mode = 'freeze'
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('Client_ip: ' + ip)
    url = 'http://' + ip + ':8000/main/sensor'
    res = Device.objects.get(ConId='B1')
    res.EnforceT_Do = True
    res.DoTemper = True
    res.save()
    # 전송 쿼리 작성
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
    # params
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


def dohumid(request):
    res = Device.objects.get(ConId='B1')
    send_Message('Request_DoHumid')
    res.EnforceH_Do = True
    res.DoHumid = True
    res.save()
    return HttpResponse("성공")


def uphumid(request):
    res = Device.objects.get(ConId='B1')
    send_Message('Request_UpHumid')
    res.EnforceH_Up = True
    res.UpHumid = True
    res.save()
    return HttpResponse("성공")


def door(request):
    return HttpResponse("성공")


def dotemp(request):
    res = Device.objects.get(ConId='B1')
    send_Message('Request_DoTemp')
    res.EnforceT_Do = True
    res.DoTemper = True
    res.save()
    return HttpResponse("성공")


def uptemp(request):
    res = Device.objects.get(ConId='B1')
    send_Message('Request_UpTemp')
    res.EnforceT_Up = True
    res.UpTemper = True
    res.save()
    return HttpResponse("성공")


def SetTempHumid(request):
    return render(request, 'chat/setting.html', {})


def SetTempHumidAct(request):
    Temp = request.POST.get('SetTemp')
    Humid = request.POST.get('SetHumid')
    res = Device.objects.get(ConId='B1')
    res.SetTemper = Temp
    res.SetHumid = Humid
    res.save()
    print('설정 온습도 변경 완료.')
    return HttpResponse("성공")


def send_Message(msg):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'status',
        {

            'type': 'chat_message',
            'con_type': msg,
            'message': msg,
            'device_num': 'manager'
        }
    )
    pass
