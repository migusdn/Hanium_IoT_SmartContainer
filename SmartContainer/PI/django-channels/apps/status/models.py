from django.db import models

class Device(models.Model):
    ConId = models.CharField(default="B1",max_length=100, null=True)
    #nodemcu 종류
    Type = models.CharField(max_length=100, null=True)
    #on/off 여부
    Stat = models.BooleanField(default=False)
    Temper = models.CharField(max_length=100, null=True)
    Humid = models.CharField(max_length=100, null=True)
    Door = models.BooleanField(default=False)
    SetTemper = models.CharField(max_length=100, null=True)
    SetHumid = models.CharField(max_length=100, null=True)
    UpTemper = models.CharField(max_length=100, null=True)
    DoTemper = models.CharField(max_length=100, null=True)
    UpHumid = models.CharField(max_length=100, null=True)
    DoHumid = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ConId
