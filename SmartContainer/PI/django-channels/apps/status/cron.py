#status/cron.py
import requests
from .models import Device
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import datetime
def update():
    res = Device.objects.get(ConId='B1')
    url = "http://192.168.0.x:8000/main/reset"
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
    print(datetime.datetime.now(), paramDict)
    requests.post(url, params=paramDict)
def init():
    res = Device.objects.get(ConId='B1')
    res.EnforceH_Do = False
    res.EnforceT_Do = False
    res.EnforceT_Up = False
    res.EnforceH_Up = False
    res.save()
    print(datetime.datetime.now(), 'init finish')
    pass
def control():
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'status',
        {
            'type': 'chat_message',
            'con_type': 'Request_TempHumid',
            'message': 'Request_TempHumid',
            'device_num': 'manager'
        }
    )
    res = Device.objects.get(ConId='B1')
    SetTemp = int(res.SetTemper)
    SetHumid = int(res.SetHumid)
    Temper = int(res.Temper)
    Humid = int(res.Humid)

    EnforceT_Up = res.EnforceT_Up
    EnforceT_Do = res.EnforceT_Do
    EnforceH_Up = res.EnforceH_Up
    EnforceH_Do = res.EnforceH_Do
    print('현재 설정온도:',SetTemp)
    print('현재 설정습도:',SetHumid)
    print('현재 온도:', Temper)
    print('현재 습도:', Humid)
    print('EnforceT_Up', str(res.EnforceT_Up))
    print('EnforceT_Do', str(res.EnforceT_Do))
    print('EnforceH_Up', str(res.EnforceH_Up))
    print('EnforceH_Do', str(res.EnforceH_Do))


    if(SetTemp > Temper):
        print('Temp lower than SetTemp')
        if(EnforceT_Do == True):
            print('Warn: TempDo Enforced')
            print('Can not run TempUp')
        elif(EnforceT_Do == False):
            res.UpTempr = True
            res.DoTemper = False
            async_to_sync(layer.group_send)(
                'status',
                {
                    'type': 'chat_message',
                    'con_type': 'Request_UpTemp',
                    'message': 'Request_UpTemp',
                    'device_num': 'manager'
                }
            )
            print('info: TempUp is run')
    elif(SetTemp < Temper):
        print('Temp higher than SetTemp')
        if (EnforceT_Up == True):
            print('Warn: TempUp Enforced')
            print('Can not run TempDo')
        elif (EnforceT_Up == False):
            res.DoTemper = True
            res.UpTempr = False
            async_to_sync(layer.group_send)(
                'status',
                {
                    'type': 'chat_message',
                    'con_type': 'Request_DoTemp',
                    'message': 'Request_DoTemp',
                    'device_num': 'manager'
                }
            )
            print('info: TempDo is run')

#습도
    if(SetHumid > Humid):
        print('Humid lower than SetHumid')
        if(EnforceH_Do == True):
            print('Warn: HumidDo Enforced')
            print('Can not run HumidUp')
        elif(EnforceH_Do == False):
            res.UpHumid = True
            res.DoHumid = False
            async_to_sync(layer.group_send)(
                'status',
                {
                    'type': 'chat_message',
                    'con_type': 'Request_UpHumid',
                    'message': 'Request_UpHumid',
                    'device_num': 'manager'
                }
            )
            print('info: HumidUp is run')
    elif(SetHumid < Humid):
        print('Humid higher than SetHumid')
        if (EnforceH_Up == True):
            print('Warn: HumidUp Enforced')
            print('Can not run HumidDo')
        elif (EnforceH_Up == False):
            res.DoHumid = True
            res.UpHumid = False
            async_to_sync(layer.group_send)(
                'status',
                {
                    'type': 'chat_message',
                    'con_type': 'Request_DoHumid',
                    'message': 'Request_DoHumid',
                    'device_num': 'manager'
                }
            )
            print('info: HumidDo is run')
    res.save()
    pass
