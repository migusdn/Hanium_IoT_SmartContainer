from django.db import models

class Device(models.Model):
    Device_num = models.IntegerField()
    Device_name = models.CharField(max_length=10)
    Device_status = models.BooleanField()

    def __str__(self):
        return self.Device_num
