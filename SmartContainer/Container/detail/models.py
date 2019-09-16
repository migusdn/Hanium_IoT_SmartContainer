from django.db import models


class Detail(models.Model):
    ContainerID = models.CharField(max_length=100, null=True)
    Temper = models.CharField(max_length=100, null=True)
    Humid = models.CharField(max_length=100, null=True)
    SetTemper = models.CharField(max_length=100, null=True)
    SetHumid = models.CharField(max_length=100, null=True)
    Door = models.CharField(max_length=100, null=True)
    UpTemper = models.CharField(max_length=100, null=True)
    DoTemper = models.CharField(max_length=100, null=True)
    UpHumid = models.CharField(max_length=100, null=True)
    DoHumid = models.CharField(max_length=100, null=True)
    StatCheck = models.CharField(default="0", max_length=100, null=True)

