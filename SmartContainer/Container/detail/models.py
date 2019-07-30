from django.db import models


class Detail(models.Model):
    ContainerID = models.CharField(max_length=200, null=True)
    Temper = models.CharField(max_length=200, null=True)
    Humid = models.CharField(max_length=200, null=True)
    Door = models.CharField(max_length=200, null=True)