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
            res.Temper = int(text_data_json['temp'])
            res.Humid = int(text_data_json['humid'])
        elif (con_type == 'test'):
            print('con_type test')
        #elif (con_type == ' ')
        elif con_type == 'error':
            print(text_data_json['message'], 'is not working')
    else:
        if mode == 'freeze':
            print('request: freeze')
            res.EnforceT_Do = True
            res.DoTemper = True
    res.save()
