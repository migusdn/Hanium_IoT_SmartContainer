from .models import Device
import requests
import json
def Node_Control(text_data, mode):
    text_data_json = json.loads(text_data)
    res = Device.objects.get(ConId='B1')
    url = 'http://127.0.0.1:8000/test'
    #connect 된 개체가 어떤 건지 구별함
    con_type = text_data_json['con_type']
    print('연결 종류',con_type)
    if con_type is not None:
        if (con_type == 'freeze'):
            print('request: freeze')
            res.EnforceT_Do = True
            res.DoTemper = True
        elif (con_type == 'TempHumid'):
            print('request: TempHumid')
            if text_data_json['message'] == 'OFF':
                res.Temper = None
                res.Humid = None
            else:
                res.Temper = text_data_json['temp']
                res.Humid = text_data_json['humid']
        elif (con_type == 'test'):
            print('con_type test')
        #elif (con_type == ' ')
    else:
        if mode == 'freeze':
            print('request: freeze')
            res.EnforceT_Do = True
            res.DoTemper = True
    res.save()

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
    #DB 덤프 보내려면 아래줄 주석해제
    #requests.get(url, params=paramDict)

def DB_dump(url):
    res = Device.objects.get(ConId='B1')
    paramDict = {
        "ConId": res.ConId,
        "Temper": res.Temper,
        "Humid": res.Humid,
        "Door": "1",
        "SetTemper": res.SetTemper,
        "SetHumid": res.SetHumid,
        "UpTemper": str(res.UpTemper),
        "DoTemper": str(res.DoTemper),
        "UpHumid": str(res.UpHumid),
        "DoHumid": str(res.DoHumid)
    }

