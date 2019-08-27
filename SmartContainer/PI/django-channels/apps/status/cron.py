#status/cron.py
from .models import Device
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
def test():
    print('Hi')
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
    pass