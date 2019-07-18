from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def device(request, device_num):
    return render(request, 'device/info.html', {
        'device_num_json': mark_safe(json.dumps(device_num))
    })
# Create your views here.
