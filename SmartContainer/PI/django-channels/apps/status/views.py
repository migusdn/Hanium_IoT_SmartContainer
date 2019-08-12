from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import viewsets
from .serializers import DeviceSerializer
from .models import Device
import requests
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    url="http://192.168.0.2:8000/main/sensor"
    paramDict = {
        "abc" : "111",
        "cde" : 123
    }
    data = "test"
    jsonp_callback = request.GET.get("callback")
    print(jsonp_callback)
    if jsonp_callback:
        response = HttpResponse("%s(%s);" % (jsonp_callback, json.dumps(data)))
        response["Content-type"] = "text/javascript; charset=utf-8"
        print('1')
    else:
        response = HttpResponse(json.dumps(data))
        response["Content-type"] = "application/json; charset=utf-8"
        print('2')
    requests.get(url, params=paramDict)
    return HttpResponse("%s(%s);" % (jsonp_callback, json.dumps(data)))
