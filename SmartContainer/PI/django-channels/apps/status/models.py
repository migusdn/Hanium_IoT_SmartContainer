from django.db import models

class Device(models.Model):
    Conid = models.CharField(default="B1")
    #nodemcu 종류
    Type = models.CharField()
    #on/off 여부
    Status = models.BooleanField()
    Temper = models.CharField()
    Humid = models.CharField()
    Door = models.BooleanField()
    SetTemper = models.CharField()
    SetHumid = models.CharField()
    UpTemper = models.CharField()
    DoTemper = models.CharField()
    UpHumid = models.CharField()
    DoHumid = models.CharField()

    def __str__(self):
        return self.Device_num
