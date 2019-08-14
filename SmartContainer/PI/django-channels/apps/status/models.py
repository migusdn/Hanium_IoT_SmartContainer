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

    #온도 상승 모듈
    UpTemper = models.NullBooleanField()
    #온도 하강 모듈 (freeze)
    DoTemper = models.NullBooleanField()

    UpHumid = models.CharField(max_length=100, null=True)
    DoHumid = models.CharField(max_length=100, null=True)
    # 강제성 유무
    EnforceT_Up = models.NullBooleanField()
    EnforceT_Do = models.NullBooleanField()
    EnforceH_Up = models.NullBooleanField()
    EnforceH_Do = models.NullBooleanField()

    def __str__(self):
        return self.ConId
